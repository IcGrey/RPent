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

"""Regression checks for the migration adapter tool boundary."""

import importlib.util
from pathlib import Path

import pytest

_path = Path(__file__).resolve().parents[4] / "migration" / "rpent_codex_tool_filter.py"
_spec = importlib.util.spec_from_file_location("migration_tool_filter", _path)
_filter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_filter)


def test_resources_and_shell_are_not_exposed_and_context_is_preserved():
    request = {
        "input": [{"role": "user", "content": "read the note"}],
        "model": "gpt-5.5",
        "tools": [
            {"type": "function", "name": "read_mcp_resource"},
            {"type": "function", "name": "exec_command"},
        ],
    }
    tools = [{"type": "function", "name": "read_text_file", "parameters": {}}]
    filtered = _filter.restrict_request(request, tools)
    assert filtered["input"] == request["input"]
    assert filtered["model"] == request["model"]
    assert filtered["tools"][0]["name"] == "mcp__rpent"
    assert filtered["tools"][0]["tools"] == tools
    assert request["tools"][0]["name"] == "read_mcp_resource"


def test_tool_free_connectivity_probe_stays_tool_free():
    assert _filter.restrict_request({"tools": [{"name": "read_mcp_resource"}]}, []) == {
        "tools": []
    }


def test_unexpected_calls_are_blocked_in_stream_items_and_final_response():
    bad = {
        "type": "function_call",
        "name": "read_mcp_resource",
        "arguments": '{"server":"codex_apps","uri":"placeholder"}',
    }
    assert not _filter.allowed_event({"item": bad}, {"read_text_file"})
    assert not _filter.allowed_event(
        {"response": {"output": [bad]}}, {"read_text_file"}
    )
    good = {
        "type": "function_call",
        "namespace": "mcp__rpent",
        "name": "read_text_file",
    }
    assert _filter.allowed_event({"item": good}, {"read_text_file"})
    assert not _filter.allowed_event(
        {"item": {**good, "name": "unknown"}}, {"read_text_file"}
    )


def test_sdk_rpent_url_override_uses_last_value():
    assert (
        _filter.mcp_url_from_args(
            [
                "app-server",
                "-c",
                'mcp_servers.rpent.url="http://localhost/old"',
                '--config=mcp_servers.rpent.url="http://localhost/new"',
            ]
        )
        == "http://localhost/new"
    )
    assert _filter.mcp_url_from_args(["app-server", "-c", 'model="gpt-5.5"']) is None


def test_new_overrides_preserve_sdk_root_mcp_configuration():
    args = ["codex", "-c", 'mcp_servers.rpent.url="http://localhost/mcp"', "app-server"]
    result = _filter.root_config_overrides(args, {"features.apps": False})
    assert result[-1] == "app-server"
    assert result[:-1] == args[:-1] + ["-c", "features.apps=false"]
    assert _filter.mcp_url_from_args(result) == "http://localhost/mcp"
    assert args[-1] == "app-server"


def test_upstream_authorization_has_only_one_case_insensitive_header():
    headers = _filter.upstream_headers(
        {"Authorization": "Bearer old", "Host": "localhost", "Content-Length": "1"},
        "synthetic-test-key",
    )
    assert headers == {
        "authorization": "Bearer synthetic-test-key",
        "accept-encoding": "identity",
    }


@pytest.mark.parametrize("error_type", ["RemoteProtocolError", "WriteTimeout"])
def test_proxy_reports_transport_failure_without_leaking_secrets(
    monkeypatch, tmp_path, error_type
):
    diagnostic_path = tmp_path / "diagnostics.jsonl"
    monkeypatch.setenv("RPENT_PROXY_DIAGNOSTICS", str(diagnostic_path))
    import httpx

    class FailingClient:
        def __init__(self, **kwargs):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def stream(self, *args, **kwargs):
            raise getattr(httpx, error_type)("secret-sentinel")

    real_client = httpx.Client
    monkeypatch.setattr(_filter.httpx, "Client", FailingClient)
    with _filter.tool_filter(
        "https://example.invalid/v1", [], "secret-sentinel"
    ) as url:
        with real_client(trust_env=False) as client:
            response = client.post(url + "/responses", json={"input": "private-input"})
    assert response.status_code == 502
    diagnostic = response.json()["error"]["diagnostic"]
    assert diagnostic["exception_type"] == error_type
    assert diagnostic["phase"] == "connect_or_wait_upstream_headers"
    assert diagnostic["response_started"] is False
    assert "secret-sentinel" not in response.text
    assert "private-input" not in response.text

    saved = diagnostic_path.read_text()
    assert error_type in saved
    assert "request_started" in saved
    assert "secret-sentinel" not in saved
    assert "private-input" not in saved


@pytest.mark.parametrize(
    ("endpoint", "stream"),
    [("responses", False), ("chat/completions", False), ("chat/completions", True)],
)
def test_upload_preserves_body_and_records_progress(
    monkeypatch, tmp_path, endpoint, stream
):
    import json
    import threading
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

    import httpx

    received = []
    response_body = (
        b'data: {"choices":[{"delta":{"tool_calls":[{"function":{"name":"view_env_state"}}]}}]}\n\n'
        b"data: [DONE]\n\n"
        if stream
        else b"{}"
    )

    class Upstream(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_POST(self):
            received.append(self.rfile.read(int(self.headers["Content-Length"])))
            self.send_response(200)
            self.send_header("Content-Length", str(len(response_body)))
            if stream:
                self.send_header("Content-Type", "text/event-stream")
            self.end_headers()
            self.wfile.write(response_body)

    path = tmp_path / "upload.jsonl"
    monkeypatch.setenv("RPENT_PROXY_DIAGNOSTICS", str(path))
    monkeypatch.setenv("RPENT_PROXY_WRITE_TIMEOUT_S", "300")
    server = ThreadingHTTPServer(("127.0.0.1", 0), Upstream)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    payload = {"input": "synthetic-private-text" * 12000, "stream": stream}
    try:
        with _filter.tool_filter(
            f"http://127.0.0.1:{server.server_port}/v1", [], "fake"
        ) as url:
            with httpx.Client(trust_env=False) as client:
                response = client.post(url + "/" + endpoint, json=payload)
        assert response.status_code == 200
        assert response.content == response_body
        assert json.loads(received[0]) == (
            {**payload, "tools": []} if endpoint == "responses" else payload
        )
        events = [json.loads(x) for x in path.read_text().splitlines()]
        progress = [x for x in events if x["event"] == "upload_progress"]
        assert progress[-1]["bytes_written_to_transport"] == len(received[0])
        assert "synthetic-private-text" not in path.read_text()
        assert any(
            x.get("stage") == "http11.send_request_body.complete" for x in events
        )
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def test_episode_proxy_preserves_child_exit_and_closes_listener(tmp_path, monkeypatch):
    import json
    import socket
    import subprocess
    import sys
    import threading
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
    from urllib.parse import urlparse

    received = []

    class Upstream(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_POST(self):
            received.append(
                json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            )
            self.send_response(200)
            self.send_header("Content-Length", "2")
            self.end_headers()
            self.wfile.write(b"{}")

    child = tmp_path / "child.py"
    child.write_text(
        "import httpx,sys\n"
        "url=sys.argv[sys.argv.index('--base-url')+1]\n"
        "print(url,flush=True)\n"
        "with httpx.Client(trust_env=False) as client:\n"
        " r=client.post(url+'/chat/completions',json={'model':'fake','messages':[]})\n"
        " assert r.status_code==200\n"
        "sys.exit(7)\n"
    )
    monkeypatch.setenv("OPENAI_API_KEY", "synthetic-secret-sentinel")
    monkeypatch.setenv("RPENT_PROXY_WRITE_TIMEOUT_S", "300")
    server = ThreadingHTTPServer(("127.0.0.1", 0), Upstream)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        root = Path(__file__).resolve().parents[4]
        result = subprocess.run(
            [
                sys.executable,
                str(root / "repro/relay_no_memory_episode.py"),
                str(tmp_path),
                sys.executable,
                str(child),
                "--base-url",
                f"http://127.0.0.1:{server.server_port}/v1",
            ],
            capture_output=True,
            text=True,
            timeout=15,
        )
        assert result.returncode == 7
        assert received == [{"model": "fake", "messages": []}]
        proxy = urlparse(result.stdout.strip())
        with socket.socket() as sock:
            assert sock.connect_ex((proxy.hostname, proxy.port)) != 0
        diagnostics = (tmp_path / "upload-diagnostics.jsonl").read_text()
        assert "synthetic-secret-sentinel" not in diagnostics
        assert '"write_timeout_s": 300.0' in diagnostics
        assert "upload_progress" in diagnostics
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
