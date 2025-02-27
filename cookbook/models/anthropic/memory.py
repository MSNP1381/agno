"""
This recipe shows how to use personalized memories and summaries in an agent.
Steps:
1. Run: `./cookbook/scripts/run_pgvector.sh` to start a postgres container with pgvector
2. Run: `pip install anthropic sqlalchemy 'psycopg[binary]' pgvector` to install the dependencies
3. Run: `python cookbook/models/anthropic/memory.py` to run the agent
"""

from agno import Agent, AgentMemory
from agno.memory.db.postgres import PgMemoryDb
from agno.models.anthropic import Claude
from agno.storage.agent.postgres import PostgresAgentStorage
from rich.pretty import pprint

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20241022"),
    # Store the memories and summary in a database
    memory=AgentMemory(
        db=PgMemoryDb(table_name="agent_memory", db_url=db_url),
        create_user_memories=True,
        create_session_summary=True,
    ),
    # Store agent sessions in a database
    storage=PostgresAgentStorage(
        table_name="personalized_agent_sessions", db_url=db_url
    ),
    # Show debug logs so, you can see the memory being created
    # debug_mode=True,
)

# -*- Share personal information
agent.print_response("My name is john billings?", stream=True)

# -*- Share personal information
agent.print_response("I live in nyc?", stream=True)

# -*- Share personal information
agent.print_response("I'm going to a concert tomorrow?", stream=True)

# Ask about the conversation
agent.print_response(
    "What have we been talking about, do you know my name?", stream=True
)
