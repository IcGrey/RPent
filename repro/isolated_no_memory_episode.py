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

"""Expose only the current episode and a read-only empty memory corpus."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

out, mem = (Path(arg).resolve() for arg in sys.argv[1:3])
command = sys.argv[3:]
root = Path(__file__).resolve().parents[1]


def mount(*args):
    subprocess.run(["mount", *map(str, args)], check=True)


mount("--make-rprivate", "/")
with tempfile.TemporaryDirectory(prefix="rpent-isolation-") as temp:
    handles = []
    for label, source, readonly in [
        ("episode", out, False),
        ("memory", mem, True),
        ("config", root / "repro/libero-config", False),
    ]:
        handle = Path(temp) / label
        handle.mkdir()
        mount("--bind", source, handle)
        handles.append((source, handle, readonly))
    for name in ("memory", "logs", "archives", "repro"):
        (root / name).mkdir(exist_ok=True)
        mount("-t", "tmpfs", "-o", "size=16m", "tmpfs", root / name)
    for source, handle, readonly in handles:
        source.mkdir(parents=True, exist_ok=True)
        mount("--bind", handle, source)
        if readonly:
            mount("-o", "remount,bind,ro", source)
        subprocess.run(["umount", str(handle)], check=True)
os.execvpe(command[0], command, os.environ)
