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

"""Read planner timeout evidence without treating arbitrary errors as timeouts."""

import re
from collections.abc import Mapping
from typing import Any


def planner_timed_out(transcript: Mapping[str, Any], console: str) -> bool:
    """Prefer the saved planner error; support logs from older transcripts.

    Elapsed time and exit code alone do not identify the cause of failure.
    """
    pattern = r"(?:planner|Codex SDK) timed out after \d+(?:\.\d+)?s"
    if "agent_error" in transcript:
        error = transcript["agent_error"]
        return isinstance(error, str) and re.fullmatch(pattern, error) is not None
    return re.search(pattern, console) is not None
