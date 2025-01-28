from agno.agent import AgentKnowledge
from agno.embedder.openai import OpenAIEmbedder
from agno.vectordb.postgres import PostgresDb

embeddings = OpenAIEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

# Print the embeddings and their dimensions
print(f"Embeddings: {embeddings[:5]}")
print(f"Dimensions: {len(embeddings)}")

# Example usage:
knowledge_base = AgentKnowledge(
    vector_db=PostgresDb(
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        table_name="openai_embeddings",
        embedder=OpenAIEmbedder(),
    ),
    num_documents=2,
)
