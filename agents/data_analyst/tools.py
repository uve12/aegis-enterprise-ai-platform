import os
import re
from pathlib import Path
import time

from agents.common.monitoring import (
    new_request_id,
    record_operation,
)

# Load this agent's .env when the module is imported directly.
# ADK also loads the agent .env during normal ADK execution.
from dotenv import load_dotenv

AGENT_DIR = Path(__file__).resolve().parent
load_dotenv(AGENT_DIR / ".env")


FORBIDDEN_SQL = {
    "insert",
    "update",
    "delete",
    "drop",
    "alter",
    "truncate",
    "create",
    "merge",
    "grant",
    "revoke",
}


def validate_read_only_sql(sql: str, allowed_table: str) -> tuple[bool, str]:
    """Reject multi-statement, non-read-only, or out-of-scope SQL."""

    normalized = sql.strip().lower()

    if not normalized:
        return False, "SQL is empty."

    # Permit one optional trailing semicolon.
    sql_without_trailing_semicolon = normalized.rstrip(";").strip()

    # Any remaining semicolon means multiple statements.
    if ";" in sql_without_trailing_semicolon:
        return False, "Multiple SQL statements are not allowed."

    # Only SELECT or WITH queries are permitted.
    first_word = re.match(r"^(\w+)", normalized)

    if not first_word:
        return False, "SQL does not contain a valid statement."

    if first_word.group(1) not in {"select", "with"}:
        return False, "Only SELECT/WITH queries are allowed."

    # Reject dangerous SQL keywords.
    for keyword in FORBIDDEN_SQL:
        if re.search(rf"\b{re.escape(keyword)}\b", normalized):
            return False, f"Forbidden SQL keyword: {keyword}."

    # Normalize the configured table.
    normalized_allowed_table = allowed_table.strip().lower()

    if not normalized_allowed_table:
        return False, "Approved BigQuery table is empty."

    # The approved table must appear in the query.
    if normalized_allowed_table not in normalized:
        return False, "Query references a table outside the approved allow-list."

    return True, "OK"

def run_read_only_query(sql: str) -> dict:
    """Execute a read-only query against the single approved orders table."""

    request_id = new_request_id()
    start_time = time.perf_counter()

    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    allowed_table = os.environ.get("AEGIS_BQ_TABLE")

    if not project_id or not allowed_table:
        record_operation(
            request_id=request_id,
            agent_name="data_analyst",
            tool_name="run_read_only_query",
            start_time=start_time,
            status="error",
            error="BigQuery configuration is missing.",
        )

        return {
            "status": "error",
            "error": "BigQuery configuration is missing.",
            "request_id": request_id,
        }

    allowed, reason = validate_read_only_sql(
        sql,
        allowed_table,
    )

    if not allowed:
        record_operation(
            request_id=request_id,
            agent_name="data_analyst",
            tool_name="run_read_only_query",
            start_time=start_time,
            status="rejected",
            error=reason,
        )

        return {
            "status": "rejected",
            "error": reason,
            "request_id": request_id,
        }

    from google.cloud import bigquery

    client = bigquery.Client(project=project_id)

    job_config = bigquery.QueryJobConfig(
        maximum_bytes_billed=100_000_000
    )

    try:
        rows = list(
            client.query(
                sql,
                job_config=job_config,
            ).result()
        )

        record_operation(
            request_id=request_id,
            agent_name="data_analyst",
            tool_name="run_read_only_query",
            start_time=start_time,
            status="success",
        )

        return {
            "status": "success",
            "rows": [dict(row.items()) for row in rows],
            "request_id": request_id,
        }

    except Exception as exc:
        record_operation(
            request_id=request_id,
            agent_name="data_analyst",
            tool_name="run_read_only_query",
            start_time=start_time,
            status="error",
            error=str(exc),
        )

        return {
            "status": "error",
            "error": str(exc),
            "request_id": request_id,
        }

def get_orders_schema() -> dict:
    """Return the schema of the approved orders table."""
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    allowed_table = os.environ.get("AEGIS_BQ_TABLE")

    if not project_id or not allowed_table:
        return {
            "status": "error",
            "error": "BigQuery configuration is missing.",
        }

    from google.cloud import bigquery

    try:
        client = bigquery.Client(project=project_id)
        table = client.get_table(allowed_table)

        return {
            "status": "success",
            "table": allowed_table,
            "columns": [
                {
                    "name": field.name,
                    "type": field.field_type,
                    "mode": field.mode,
                }
                for field in table.schema
            ],
        }

    except Exception as exc:
        return {
            "status": "error",
            "error": str(exc),
        }