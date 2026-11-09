import os
from langchain_postgres.vectorstores import PGVector
from langchain_openai import OpenAIEmbeddings

# Read OPENAI_API_KEY from the environment; never commit API credentials.
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("Set the OPENAI_API_KEY environment variable before running this script.")

# Initialize the OpenAI embeddings
embeddings = OpenAIEmbeddings()

# PostgreSQL connection details
connection_url = "postgresql+psycopg://your_username:your_password@localhost:5432/ads_db"

# Initialize the PGVector vector store
vectorstore = PGVector(
    embeddings=embeddings,
    collection_name="ads_collection",
    connection=connection_url,
    use_jsonb=True,
)

# Perform a similarity search
query = "food delivery service"
results = vectorstore.similarity_search(query, k=5)

# Print the results
for result in results:
    print(f"Description: {result.page_content}")
    print(f"Keywords: {result.metadata['keywords']}")
    print()
