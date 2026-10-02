import os

from google.adk.agents import Agent

from .tools import get_incident


MODEL = os.environ.get("AEGIS_MODEL", "gemini-2.5-flash")


root_agent = Agent(
    name="incident_agent",
    model=MODEL,
    description="Investigates documented NovaRetail incidents.",
    instruction="""
You are the NovaRetail Incident Agent.

Always call get_incident before discussing a specific incident.
Use documented evidence from the tool.
Clearly distinguish documented facts from analysis.
Never invent a root cause, severity, timeline, or remediation.
""",
    tools=[get_incident]
)
