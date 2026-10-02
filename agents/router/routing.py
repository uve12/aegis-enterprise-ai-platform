DATA_TERMS = {
    "revenue",
    "sales",
    "order",
    "orders",
    "customer",
    "customers",
    "product",
    "products",
    "category",
    "categories",
    "amount",
}

INCIDENT_TERMS = {
    "incident",
    "outage",
    "error",
    "failure",
    "production",
    "root cause",
    "500",
    "timeout",
}

KNOWLEDGE_TERMS = {
    "policy",
    "policies",
    "procedure",
    "procedures",
    "documentation",
    "refund policy",
}


def fast_route(query: str) -> str | None:
    """
    Route obvious requests without an LLM.

    Returns:
        DATA
        KNOWLEDGE
        INCIDENT
        None -> ambiguous; use Gemini router
    """
    q = query.lower()

    if any(term in q for term in DATA_TERMS):
        return "DATA"

    if any(term in q for term in INCIDENT_TERMS):
        return "INCIDENT"

    if any(term in q for term in KNOWLEDGE_TERMS):
        return "KNOWLEDGE"

    return None