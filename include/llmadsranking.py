import openai
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Set your OpenAI API key
openai.api_key = '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'

# Initialize the LangChain ChatOpenAI model
model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai.api_key)

# Function to read text from a file
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to generate ad recommendations using LangChain
def generate_ad_recommendations(text):
    messages = [
        SystemMessage(content="In JSON Format Based on the following text, can we extract 3 keywords for advertisement recommendation product or service."),
        HumanMessage(content=text),
    ]
    response = model.invoke(messages)
    #print(response.content.strip())
    return response.content.strip()

# Read the text file
# #file_path = 'input.txt'  # Ensure the file is uploaded to your Jupyter/Colab environment
# text = result["text"]