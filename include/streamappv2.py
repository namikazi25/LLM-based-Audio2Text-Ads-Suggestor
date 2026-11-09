import streamlit as st
import os
from pydub import AudioSegment
from transcribe import transcribe
from llmadsranking import generate_ad_recommendations
from create_retriever import retrieve_ads
from generate_response import generate_response
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
import av

# Configure OPENAI_API_KEY in the environment before starting this app.
if not os.getenv("OPENAI_API_KEY"):
    st.error("Set the OPENAI_API_KEY environment variable before starting the app.")
    st.stop()

# Streamlit interface
st.title("RAG-based Ad Recommendation System")

# Class to handle audio processing
class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.audio_frames = []

    def recv(self, frame):
        audio = frame.to_ndarray()
        self.audio_frames.append(audio)
        return av.AudioFrame.from_ndarray(audio, layout="mono")

# Function to save audio frames to a file
def save_audio(frames, filename, sample_rate=44100):
    audio_segment = AudioSegment(
        data=b''.join(frames),
        sample_width=2,  # Assuming 16-bit audio
        frame_rate=sample_rate,
        channels=1
    )
    audio_segment.export(filename, format="wav")

# Option to upload audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
if uploaded_file is not None:
    # Save the uploaded file
    file_path = f"uploaded_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.audio(file_path, format="audio/mp3")
    
    if st.button("Process Uploaded Audio"):
        # Step 1: Transcribe audio to text
        text = transcribe(file_path)
        st.write("Transcribed Text:")
        st.write(text)
        
        # Step 2: Generate ranked keywords JSON
        ad_recommendations = generate_ad_recommendations(text)
        st.write("Ranked Keywords JSON:")
        st.json(ad_recommendations)
        
        # Step 3: Retrieve relevant ads
        retrieved_ads = retrieve_ads(ad_recommendations)
        
        # Step 4: Generate response based on retrieved ads
        response = generate_response(retrieved_ads)
        
        # Display the retrieved ads and the generated response
        st.write("Retrieved Ads:")
        for ad in retrieved_ads:
            st.write(f"Description: {ad.page_content}")
            st.write(f"Keywords: {ad.metadata['keywords']}")
            st.write(f"Link: {ad.metadata.get('link', 'No link provided')}")
            st.write("---")
        
        st.write("Generated Response:")
        st.write(response)

# Option to record audio using microphone
st.write("Or record audio using your microphone:")

webrtc_ctx = webrtc_streamer(key="audio", mode=WebRtcMode.SENDONLY, audio_processor_factory=AudioProcessor)

if st.button("Process Recorded Audio"):
    if webrtc_ctx.audio_processor:
        audio_processor = webrtc_ctx.audio_processor
        if audio_processor.audio_frames:
            # Save the recorded audio
            frames = [frame.tobytes() for frame in audio_processor.audio_frames]
            save_audio(frames, "recorded_audio.wav")
            
            # Step 1: Transcribe audio to text
            text = transcribe("recorded_audio.wav")
            st.write("Transcribed Text:")
            st.write(text)
            
            # Step 2: Generate ranked keywords JSON
            ad_recommendations = generate_ad_recommendations(text)
            st.write("Ranked Keywords JSON:")
            st.json(ad_recommendations)
            
            # Step 3: Retrieve relevant ads
            retrieved_ads = retrieve_ads(ad_recommendations)
            
            # Step 4: Generate response based on retrieved ads
            response = generate_response(retrieved_ads)
            
            # Display the retrieved ads and the generated response
            st.write("Retrieved Ads:")
            for ad in retrieved_ads:
                st.write(f"Description: {ad.page_content}")
                st.write(f"Keywords: {ad.metadata['keywords']}")
                st.write(f"Link: {ad.metadata.get('link', 'No link provided')}")
                st.write("---")
            
            st.write("Generated Response:")
            st.write(response)
