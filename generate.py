from huggingface_hub import InferenceClient
import streamlit as st

def generate_banner(prompt):
    api_key = st.secrets["HUGGINGFACE_API_TOKEN"]
    # Initialize without specifying the model in the client
    client = InferenceClient(token=api_key)
    
    # Force the use of the specific model via the API endpoint
    image = client.text_to_image(prompt, model="runwayml/stable-diffusion-v1-5")
    return image
