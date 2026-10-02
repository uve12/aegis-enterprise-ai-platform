import os

from dotenv import load_dotenv
from google import genai
load_dotenv()



PROJECT_ID = os.environ["GOOGLE_CLOUD_PROJECT"]
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain what an enterprise AI agent is in three sentences.",
)

print(response.text)
