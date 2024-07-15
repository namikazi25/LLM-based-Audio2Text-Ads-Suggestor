import os
import psycopg2
from langchain_postgres.vectorstores import PGVector
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = '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'

# Initialize the OpenAI embeddings
embeddings = OpenAIEmbeddings()

# PostgreSQL connection details
connection_url = "postgresql+psycopg://your_username1:your_password1@localhost:5432/ads_dbv1"

# Connect to PostgreSQL database using psycopg2
conn = psycopg2.connect(
    dbname="ads_db",
    user="your_username",
    password="your_password",
    host="localhost"
)
cursor = conn.cursor()

# Fetch ads data from PostgreSQL
cursor.execute("SELECT description, keywords, link FROM ads")
ads = cursor.fetchall()

# Convert ads data to Document objects
docs = [
    Document(page_content=ad[0], metadata={"keywords": ad[1], "link": ad[2]})
    for ad in ads
]

# Create and populate the PGVector vector store
vectorstore = PGVector.from_documents(
    documents=docs,
    embedding=embeddings,
    connection=connection_url,
    collection_name="ads_collection",
    use_jsonb=True
)

# Commit and close the connection
conn.commit()
cursor.close()
conn.close()
