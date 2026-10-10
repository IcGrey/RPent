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

"""Run one isolated episode through the instrumented upload proxy."""

import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    output = Path(sys.argv[1]).resolve()
    command = sys.argv[2:]
    root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root))
    from migration.rpent_codex_tool_filter import tool_filter

    index = command.index("--base-url") + 1
    upstream = command[index]
    os.environ["RPENT_PROXY_DIAGNOSTICS"] = str(output / "upload-diagnostics.jsonl")
    # This process owns the proxy; the episode child shares its process group.
    # Closing the context stops the listener, then process exit closes all sockets.
    with tool_filter(upstream, [], os.environ["OPENAI_API_KEY"]) as local_url:
        command[index] = local_url
        return subprocess.run(command, check=False).returncode


if __name__ == "__main__":
    sys.exit(main())
