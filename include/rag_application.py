import streamlit as st
import os
from create_retriever import retrieve_ads
from generate_response import generate_response

# Streamlit interface
st.title("RAG-based Ad Recommendation System")

query = st.text_input("Enter your query:")
if st.button("Submit"):
    if query:
        # Retrieve relevant ads
        retrieved_ads = retrieve_ads(query)
        
        # Generate response based on retrieved ads
        response = generate_response(retrieved_ads)
        
        # Display the retrieved ads
        st.write("Retrieved Ads:")
        for ad in retrieved_ads:
            st.write(f"Description: {ad.page_content}")
            st.write(f"Keywords: {ad.metadata['keywords']}")
            st.write(f"Link: {ad.metadata.get('link', 'No link provided')}")
            st.write("---")
        
        # Display the generated response
        st.write("Generated Response:")
        st.write(response)
    else:
        st.write("Please enter a query.")
