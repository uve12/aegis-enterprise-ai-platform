import os

from google.adk.agents import Agent

from knowledge.agent import root_agent as knowledge_agent
from data_analyst.agent import root_agent as data_agent
from incident.agent import root_agent as incident_agent
from multimodal.agent import root_agent as multimodal_agent


MODEL = os.environ.get("AEGIS_MODEL", "gemini-2.5-flash")


root_agent = Agent(
    name="aegis_supervisor",
    model=MODEL,
    description="Routes enterprise requests to specialized Aegis agents.",
    instruction="""
You are the Aegis Supervisor.

Delegate:
- company policies and internal documents -> Knowledge Agent
- business analytics and orders data -> Data Analyst
- incident investigation -> Incident Agent
- Multi Media -> Multimodal agent.

Do not answer a specialist question from your own general knowledge
when a specialist is available.
Do not bypass specialist security controls.
""",
    sub_agents=[knowledge_agent, data_agent, incident_agent, multimodal_agent],
)
