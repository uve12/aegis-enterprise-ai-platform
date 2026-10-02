from google.adk.agents import Agent


root_agent = Agent(
    name="multimodal_agent",
    model="gemini-2.5-flash",
    description="Analyzes text, images, audio and video.",
    instruction="""
You are the Aegis Multimodal Agent.

Analyze the supplied media carefully.

Separate observations from assumptions.

If the media does not contain enough information,
say so clearly.
""",
)
