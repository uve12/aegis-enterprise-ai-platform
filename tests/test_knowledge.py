from agents.aegis.knowledge.tools import search_company_documents


def test_refund_policy_is_retrievable():
    result = search_company_documents("refund policy damaged products")
    assert result["status"] == "success"
    assert result["results"][0]["document"] == "refund_policy.txt"


def test_unknown_policy_is_not_invented_by_tool():
    result = search_company_documents("employee stock option vesting")
    assert result["status"] == "not_found"
