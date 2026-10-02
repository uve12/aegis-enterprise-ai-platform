import os

from google.adk.agents import Agent

from .knowledge.agent import root_agent as knowledge_agent
from .data_analyst.agent import root_agent as data_agent
from .incident.agent import root_agent as incident_agent
from .multimodal.agent import root_agent as multimodal_agent
from .mcp_demo.agent import root_agent as mcp_demo_agent


MODEL = os.environ.get("AEGIS_MODEL", "gemini-2.5-flash")


root_agent = Agent(
    name="aegis_enterprise",
    model=MODEL,
    description="NovaRetail enterprise AI operations and knowledge copilot.",
    instruction="""
You are Aegis, the enterprise AI operations and knowledge copilot.

Delegate to the appropriate specialist:
- Knowledge Agent: internal policies and documents.
- Data Analyst: approved business analytics.
- Incident Agent: documented incident investigation.
- Multimodal Agent: image, audio, and video analysis.

Never bypass a specialist's security boundary.
Never invent enterprise facts.
""",
    sub_agents=[
        knowledge_agent,
        data_agent,
        incident_agent,
        multimodal_agent,
        mcp_demo_agent,
    ],
)
