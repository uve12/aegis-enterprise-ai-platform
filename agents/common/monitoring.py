import logging
import time
import uuid
from datetime import datetime, timezone


logger = logging.getLogger("aegis.monitoring")


def new_request_id() -> str:
    return f"req-{uuid.uuid4().hex[:12]}"


def record_operation(
    *,
    request_id: str,
    agent_name: str,
    tool_name: str,
    start_time: float,
    status: str,
    error: str | None = None,
) -> dict:
    latency_ms = round(
        (time.perf_counter() - start_time) * 1000,
        2,
    )

    event = {
        "request_id": request_id,
        "agent_name": agent_name,
        "tool_name": tool_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "latency_ms": latency_ms,
        "status": status,
        "error": error,
    }

    # Never log secrets, tokens, credentials, API keys,
    # authorization headers, or document contents.
    logger.info(event)

    return event