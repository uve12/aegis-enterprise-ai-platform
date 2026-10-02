import time

from ..common.monitoring import (
    new_request_id,
    record_operation,
)

from .retrieval import search_documents


def search_company_documents(query: str) -> dict:
    request_id = new_request_id()
    start_time = time.perf_counter()

    try:
        results = search_documents(query)

        if not results:
            record_operation(
                request_id=request_id,
                agent_name="knowledge_agent",
                tool_name="search_company_documents",
                start_time=start_time,
                status="not_found",
            )

            return {
                "status": "not_found",
                "results": [],
                "request_id": request_id,
            }

        record_operation(
            request_id=request_id,
            agent_name="knowledge_agent",
            tool_name="search_company_documents",
            start_time=start_time,
            status="success",
        )

        return {
            "status": "success",
            "results": results[:5],
            "request_id": request_id,
        }

    except Exception as exc:
        record_operation(
            request_id=request_id,
            agent_name="knowledge_agent",
            tool_name="search_company_documents",
            start_time=start_time,
            status="error",
            error=str(exc),
        )

        return {
            "status": "error",
            "error": "Document search failed.",
            "request_id": request_id,
        }
