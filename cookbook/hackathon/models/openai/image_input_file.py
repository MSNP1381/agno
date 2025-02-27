from pathlib import Path

from agno import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

image_path = Path(__file__).parent.parent.parent.joinpath("data/sample_image.jpg")

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[
        Image(filepath=image_path),
    ],
    stream=True,
)
