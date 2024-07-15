import os
from langchain_postgres.vectorstores import PGVector
from langchain_openai import OpenAIEmbeddings

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = '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'

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
