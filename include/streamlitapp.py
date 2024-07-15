import streamlit as st
import os
from transcribe import transcribe
from llmadsranking import generate_ad_recommendations
from create_retriever import retrieve_ads
from generate_response import generate_response

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = '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'

# Streamlit interface
st.title("RAG-based Ad Recommendation System")

uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
if uploaded_file is not None:
    # Save the uploaded file
    with open("uploaded_audio.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.audio("uploaded_audio.mp3", format="audio/mp3")
    
    if st.button("Process Audio"):
        # Step 1: Transcribe audio to text
        text = transcribe("uploaded_audio.mp3")
        st.write("Transcribed Text:")
        st.write(text)
        
        # Step 2: Generate ranked keywords JSON
        ad_recommendations = generate_ad_recommendations(text)
        st.write("Ranked Keywords")
        st.write('ad_recommendations: ' + str(ad_recommendations))
        #st.json(ad_recommendations)
        
        # Step 3: Retrieve relevant ads
        retrieved_ads = retrieve_ads(ad_recommendations)
        print('retrieved ads' + str(retrieved_ads))
        # Step 4: Generate response based on retrieved ads
        response = generate_response(retrieved_ads)
        # Display the retrieved ads and the generated response
        st.write("Retrieved Ads:")
        for ad in retrieved_ads:
            st.write(f"Description: {ad.page_content}")
            st.write(f"Keywords: {ad.metadata['keywords']}")
            st.write(f"Link: {ad.metadata.get('link', 'No link provided')}")
            st.write("---")
            if "link" in ad.metadata:
                st.video(ad.metadata['link'])
        
        # st.write("Generated Response:")
        # st.write(response)
