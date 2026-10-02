import os
import sys
from pathlib import Path

from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters


MODEL = os.environ.get("AEGIS_MODEL", "gemini-2.5-flash")
MCP_SERVER = Path(__file__).resolve().with_name("mcp_server.py")


mcp_toolset = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command=sys.executable,
            args=[str(MCP_SERVER)],
            env=dict(os.environ),
        ),
        timeout=30,
    ),
    tool_filter=["get_incident", "search_company_documents"],
    tool_name_prefix="mcp_",
)


root_agent = Agent(
    name="mcp_demo_agent",
    model=MODEL,
    description="Demonstrates secure MCP tool integration with Aegis.",
    instruction="""
Use the MCP tools for company-document and incident questions.
Never claim that an MCP operation succeeded unless the MCP tool returned success.
Never invent incident data.
""",
    tools=[mcp_toolset],
)
