"""Free-tier key pool: rotate multiple keys, fallback across providers.

.env example:
  GOOGLE_API_KEYS=key1,key2,key3   # comma-separated, round-robin
  GROQ_API_KEY=gsk_...             # optional fallback (also free, no card)
"""
import itertools
import threading

_lock = threading.Lock()
_cycle = None
_cycle_keys: tuple = ()


def google_keys() -> list[str]:
    from app.core.config import get_settings

    s = get_settings()
    raw = s.google_api_keys or s.google_api_key or ""
    keys = [k.strip().strip('"').strip("'") for k in raw.split(",")]
    return [k for k in keys if k]


def next_google_key() -> str:
    """Round-robin ekta key dao, jate free rate-limit (15 RPM) ভাগ hoy."""
    global _cycle, _cycle_keys
    keys = google_keys()
    if not keys:
        raise RuntimeError(
            "GOOGLE_API_KEY(S) is missing. Free key nao: "
            "https://aistudio.google.com/apikey ar .env e bosao. "
            "Multiple: GOOGLE_API_KEYS=key1,key2,key3"
        )
    with _lock:
        if tuple(keys) != _cycle_keys:
            _cycle_keys = tuple(keys)
            _cycle = itertools.cycle(_cycle_keys)
        return next(_cycle)


def groq_key() -> str:
    from app.core.config import get_settings

    return (get_settings().groq_api_key or "").strip()
