import os
from google.adk.agents import Agent

from .tools import get_company_name

MODEL = os.environ.get("AEGIS_MODEL")

root_agent = Agent(
    name="hello_agent",
    model=MODEL,
    description="A simple enterprise assistant.",
    instruction="""
You are Aegis, an enterprise AI assistant.

Use tools when they are useful.

Never invent company information.
""",
    tools=[get_company_name],
)
