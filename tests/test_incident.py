from agents.aegis.incident.tools import get_incident


def test_known_incident():
    result = get_incident("INC001")
    assert result["status"] == "success"
    assert result["severity"] == "SEV2"


def test_unknown_incident():
    result = get_incident("INC999")
    assert result["status"] == "not_found"
