import os
import psycopg2
from langchain_postgres.vectorstores import PGVector
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = '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'

# Initialize the OpenAI embeddings
embeddings = OpenAIEmbeddings()

# Connect to PostgreSQL database
# PostgreSQL connection details
conn_info = "dbname=ads_db user=your_username password=your_password host=localhost port=5432"
conn = psycopg2.connect(conn_info)
cursor = conn.cursor()

# Fetch ads data from PostgreSQL
cursor.execute("SELECT description, keywords FROM ads")
ads = cursor.fetchall()

# Convert ads data to Document objects
docs = [
    Document(page_content=ad[0], metadata={"keywords": ad[1], "link": ad[2]})
    for ad in ads
]

# Create a PGVector vector store
vectorstore = PGVector(
    embeddings=embeddings,
    collection_name="ads_collection",
    connection=conn_info,
    use_jsonb=True,
)

# Add documents to the vector store
vectorstore.add_documents(docs)

# Commit and close the connection
conn.commit()
cursor.close()
conn.close()
