from langchain_openai import OpenAI
from langchain.schema import HumanMessage, SystemMessage

# Initialize the OpenAI LLM
llm = OpenAI(temperature=0)

# Function to generate a response using the LLM
def generate_response(retrieved_ads):
    messages = [
        SystemMessage(content="Here are some relevant ads based on the query:"),
        HumanMessage(content="\n".join([ad.page_content for ad in retrieved_ads])),
    ]
    response = llm.invoke(messages)
    return response  # Assuming response is already a string
