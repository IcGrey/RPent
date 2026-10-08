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
