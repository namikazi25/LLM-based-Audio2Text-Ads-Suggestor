import os
from langchain_postgres.vectorstores import PGVector
from langchain_openai import OpenAIEmbeddings
import random

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

#Function to retrieve ads based on a query
# def retrieve_ads(query):
#     # Perform a similarity search using the query
#     results = vectorstore.similarity_search(query, k=5)
#     return results

# # Function to retrieve ads based on a query
# def retrieve_ads(query):
#     # Perform a similarity search using the query
#     results = vectorstore.similarity_search(query, k=5)
#     # Filter results to include only ads with a link
#     results_with_links = [result for result in results if "link" in result.metadata and result.metadata["link"]]
#     return results_with_links



def retrieve_ads(query):
    # Perform a similarity search using the query
    results = vectorstore.similarity_search(query, k=5)  # Retrieve more results initially
    # Filter results to include only ads with a link
    results_with_links = [result for result in results if "link" in result.metadata and result.metadata["link"]]
    # Randomly sample 5 results from the filtered results to introduce diversity
    sampled_results = random.sample(results_with_links, min(len(results_with_links), 3))
    return sampled_results

# Debug function to test retrieval
def test_retrieve_ads():
    test_query = "laptop computer"
    ads = retrieve_ads(test_query)
    print(ads)
    for ad in ads:
        print(f"Description: {ad.page_content}")
        print(f"Keywords: {ad.metadata['keywords']}")
        print(f"Link: {ad.metadata.get('link', 'No link provided')}")
        print("---")

# Uncomment the line below to run the debug function when the script is executed
test_retrieve_ads()