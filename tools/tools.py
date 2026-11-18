import pathlib
import json
import valkey

ROOT = pathlib.Path("./data").resolve()


def _safe(path: str) -> pathlib.Path:
    p = (ROOT / path).resolve()
    if not p.is_relative_to(ROOT):
        raise ValueError("path outside workspace")
    return p


def read_file(path: str) -> str:
    """Read a text file and return its contents."""
    return _safe(path).read_text()[:20000]


def write_file(path: str, content: str) -> str:
    """Write content to a file, creating it if needed."""
    p = _safe(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)
    return f"wrote {len(content)} chars to {path}"


def extract_facts() -> dict:
    """Fetches all the cached session context history of itself from ValKey by using a key pattern scan and fetch each key's content and return the facts of the previous chat sessions."""
    r = valkey.Valkey(host="localhost", port=6379, decode_responses=True)
    sessions = {}
    for key in r.scan_iter(match="session_id:*", count=100):
        raw = r.get(key)
        if raw:
            sessions[key.removeprefix("session_id:")] = json.loads(raw)
    return sessions
