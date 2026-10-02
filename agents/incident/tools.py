import time

from agents.common.monitoring import (
    new_request_id,
    record_operation,
)


INCIDENTS = {
    "INC001": {
        "service": "Checkout API",
        "severity": "SEV2",
        "status": "Resolved",
        "description": "Elevated API latency caused checkout delays.",
        "root_cause": "A database connection pool configuration caused request queuing.",
    },
    "INC002": {
        "service": "Payments",
        "severity": "SEV1",
        "status": "Resolved",
        "description": "Payment requests intermittently failed.",
        "root_cause": "A downstream payment provider experienced an outage.",
    },
    "INC003": {
        "service": "Search",
        "severity": "SEV3",
        "status": "Resolved",
        "description": "Search indexing was delayed.",
        "root_cause": "Indexer workers were temporarily under-provisioned.",
    },
}


def get_incident(incident_id: str) -> dict:
    """Return documented information for a known incident."""

    request_id = new_request_id()
    start_time = time.perf_counter()

    try:
        incident = INCIDENTS.get(incident_id.upper())

        if incident is None:
            record_operation(
                request_id=request_id,
                agent_name="incident_agent",
                tool_name="get_incident",
                start_time=start_time,
                status="not_found",
            )

            return {
                "status": "not_found",
                "incident_id": incident_id,
                "request_id": request_id,
            }

        record_operation(
            request_id=request_id,
            agent_name="incident_agent",
            tool_name="get_incident",
            start_time=start_time,
            status="success",
        )

        return {
            **incident,
            "status": "success",
            "incident_id": incident_id.upper(),
            "request_id": request_id,
        }

    except Exception as exc:
        record_operation(
            request_id=request_id,
            agent_name="incident_agent",
            tool_name="get_incident",
            start_time=start_time,
            status="error",
            error=str(exc),
        )

        return {
            "status": "error",
            "error": "Incident lookup failed.",
            "request_id": request_id,
        }