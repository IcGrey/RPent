# Copyright 2026 The RPent Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Expose only the connected RPent MCP tools to the lab planner."""

import json
import threading
import tomllib
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import httpx
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


def mcp_url_from_args(args):
    """Find the RPent URL in the Codex SDK's CLI config overrides."""
    overrides = []
    for index, arg in enumerate(args):
        if arg in ("-c", "--config") and index + 1 < len(args):
            overrides.append(args[index + 1])
        elif arg.startswith("--config="):
            overrides.append(arg.removeprefix("--config="))
    url = None
    for override in overrides:
        key, separator, value = override.partition("=")
        if separator and key == "mcp_servers.rpent.url":
            url = tomllib.loads("url=" + value)["url"]
    return url


async def load_tools(url):
    async with httpx.AsyncClient(timeout=20, trust_env=False) as client:
        async with streamable_http_client(url, http_client=client) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                await session.initialize()
                result = await session.list_tools()
                return [
                    {
                        "type": "function",
                        "name": tool.name,
                        "description": tool.description or "",
                        "parameters": tool.inputSchema,
                        "strict": False,
                    }
                    for tool in result.tools
                ]


def restrict_request(payload, tools):
    """Eagerly expose RPent tools; discard Codex's unrelated tool catalog."""
    return {
        **payload,
        "tools": [
            {
                "type": "namespace",
                "name": "mcp__rpent",
                "description": "Tools exposed by the connected RPent runtime.",
                "tools": tools,
            }
        ]
        if tools
        else [],
    }


def allowed_event(event, names):
    """Reject unexpected executable tool calls before Codex can dispatch them."""
    items = []
    if isinstance(event.get("item"), dict):
        items.append(event["item"])
    if isinstance(event.get("response"), dict):
        items.extend(event["response"].get("output", []))
    for item in items:
        kind = item.get("type")
        if kind == "function_call":
            name = item.get("name")
            if not (
                (item.get("namespace") == "mcp__rpent" and name in names)
                or name in {"mcp__rpent__" + n for n in names}
            ):
                return False
        elif kind in (
            "custom_tool_call",
            "tool_search_call",
            "mcp_call",
            "web_search_call",
        ):
            return False
    return True


def root_config_overrides(args, overrides):
    """Insert overrides before app-server without replacing SDK configuration."""
    extra = []
    for key, value in overrides.items():
        extra.extend(["-c", f"{key}={json.dumps(value)}"])
    index = args.index("app-server") if "app-server" in args else len(args)
    return args[:index] + extra + args[index:]


def upstream_headers(headers, api_key):
    """Replace authorization case-insensitively to avoid duplicate credentials."""
    result = {
        key.lower(): value
        for key, value in headers.items()
        if key.lower()
        not in ("host", "content-length", "connection", "accept-encoding")
    }
    result["accept-encoding"] = "identity"
    result["authorization"] = "Bearer " + api_key
    return result


@contextmanager
def tool_filter(upstream, tools, api_key):
    """Run a loopback Responses proxy without logging requests or credentials."""
    names = {tool["name"] for tool in tools}

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, *args):
            pass

        def do_POST(self):
            started = False
            try:
                body = self.rfile.read(int(self.headers.get("Content-Length", "0")))
                path = self.path.removeprefix("/v1")
                if path.rstrip("/") == "/responses":
                    body = json.dumps(
                        restrict_request(json.loads(body), tools)
                    ).encode()
                headers = upstream_headers(self.headers, api_key)
                with httpx.Client(timeout=httpx.Timeout(120, read=3700)) as client:
                    with client.stream(
                        "POST",
                        upstream.rstrip("/") + path,
                        content=body,
                        headers=headers,
                    ) as response:
                        self.send_response(response.status_code)
                        content_type = response.headers.get(
                            "content-type", "application/json"
                        )
                        self.send_header("Content-Type", content_type)
                        self.send_header("Connection", "close")
                        self.end_headers()
                        started = True
                        self.close_connection = True
                        if "text/event-stream" in content_type:
                            for line in response.iter_lines():
                                if line.startswith("data: ") and line[6:] != "[DONE]":
                                    event = json.loads(line[6:])
                                    if not allowed_event(event, names):
                                        error = {
                                            "type": "error",
                                            "code": "rpent_tool_not_allowed",
                                            "message": "The planner returned a non-RPent tool call",
                                        }
                                        self.wfile.write(
                                            (
                                                "data: " + json.dumps(error) + "\n\n"
                                            ).encode()
                                        )
                                        self.wfile.flush()
                                        return
                                self.wfile.write((line + "\n").encode())
                                self.wfile.flush()
                        else:
                            self.wfile.write(response.read())
            except (OSError, ValueError, httpx.HTTPError):
                if not started:
                    self.send_response(502)
                    self.send_header("Connection", "close")
                    self.end_headers()
                    self.wfile.write(
                        b'{"error":{"message":"RPent tool filter request failed"}}'
                    )
                self.close_connection = True

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    server.daemon_threads = True
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/v1"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)
