"""Distinguish a planner budget deadline from an infrastructure exit."""
import re


def classify_exit(code, console):
    """Only recognize the planner's explicit deadline, not arbitrary timeouts."""
    deadline = bool(re.search(
        r'^\[codex-planner\] Codex SDK timed out after \d+(?:\.\d+)?s\s*$',
        console, re.MULTILINE,
    ))
    if code == 0:
        return 'completed'
    if code in (1, None) and deadline:
        return 'planner_timeout'
    return 'infrastructure_error' if code is not None else 'unknown_exit'
