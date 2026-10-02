import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / "agents"
if str(AGENTS_DIR) not in sys.path:
    sys.path.insert(0, str(AGENTS_DIR))


from agents.aegis.agent import root_agent


def test_supervisor_graph():
    assert root_agent.name == "aegis_enterprise"
    assert [agent.name for agent in root_agent.sub_agents] == [
    "knowledge_agent",
    "data_analyst",
    "incident_agent",
    "multimodal_agent",
    "mcp_demo_agent",
]