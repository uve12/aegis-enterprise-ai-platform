from mcp.server.mcpserver import MCPServer

mcp = MCPServer("aegis-enterprise-tools")

INCIDENTS = {
    "INC001": {
        "service": "Checkout API",
        "severity": "SEV2",
        "status": "Resolved",
        "description": "Elevated API latency caused checkout delays.",
    },
}


@mcp.tool()
def get_incident(incident_id: str) -> dict:
    """Return documented information for a known incident."""
    incident = INCIDENTS.get(incident_id.upper())
    if incident is None:
        return {"status": "not_found", "incident_id": incident_id}
    return {**incident, "status": "success", "incident_id": incident_id.upper()}


@mcp.tool()
def search_company_documents(query: str) -> dict:
    """Return a deterministic demonstration response for MCP testing."""
    normalized = query.lower()
    if "refund" in normalized or "policy" in normalized:
        return {
            "status": "success",
            "source": "refund_policy.txt",
            "content": "Customers can request a refund within 30 calendar days of delivery.",
        }
    return {"status": "not_found", "query": query}


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8001,
    )