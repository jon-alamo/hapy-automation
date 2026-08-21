"""Found for real via a live Telegram conversation: OpenAI rejected a
request outright with "messages with role 'tool' must be a response to a
preceding message with 'tool_calls'" — because the naive
`history[-MAX_HISTORY_MESSAGES:]` truncation had cut in the middle of an
assistant(tool_calls) -> tool pairing, leaving a stored history that
*starts* with an orphaned tool message. _safe_truncate_history must never
do that.
"""
from custom_components.hapy_automation.agent.runner import _safe_truncate_history


def _turn(i):
    """One complete user -> assistant(tool_calls) -> tool turn."""
    return [
        {'role': 'user', 'content': f'msg{i}'},
        {'role': 'assistant', 'content': None, 'tool_calls': [{'id': f'call{i}'}]},
        {'role': 'tool', 'tool_call_id': f'call{i}', 'content': 'result'},
    ]


def test_truncation_never_starts_with_an_orphaned_tool_message():
    history = [m for i in range(10) for m in _turn(i)]

    trimmed = _safe_truncate_history(history, 5)

    assert trimmed  # non-empty
    assert trimmed[0]['role'] == 'user'
    # Every tool message in the trimmed result still has its assistant
    # tool_calls message immediately before it.
    for i, message in enumerate(trimmed):
        if message['role'] == 'tool':
            assert trimmed[i - 1]['role'] == 'assistant'
            assert trimmed[i - 1].get('tool_calls')


def test_short_history_is_returned_unchanged():
    history = [{'role': 'user', 'content': 'hi'}, {'role': 'assistant', 'content': 'hello'}]
    assert _safe_truncate_history(history, 40) == history


def test_no_user_message_in_window_returns_empty_rather_than_invalid():
    # A single pathological turn longer than max_len, with no `user`
    # message anywhere in the truncation window.
    history = [
        {'role': 'assistant', 'content': None, 'tool_calls': [{'id': 'c1'}]},
        {'role': 'tool', 'tool_call_id': 'c1', 'content': 'r1'},
        {'role': 'assistant', 'content': None, 'tool_calls': [{'id': 'c2'}]},
        {'role': 'tool', 'tool_call_id': 'c2', 'content': 'r2'},
    ]
    assert _safe_truncate_history(history, 2) == []
