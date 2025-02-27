from agno import Agent, RunResponse  # noqa
from agno.models.mistral import MistralChat


agent = Agent(
    model=MistralChat(id="mistral-large-latest"),
    markdown=True,
)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story")
# print(run.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story")
