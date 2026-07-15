import streamlit as st
from huggingface_hub import InferenceClient

def generate_banner(prompt):
    api_key = st.secrets["HUGGINGFACE_API_TOKEN"]
    # This uses the official, simplified client
    client = InferenceClient(api_key=api_key)
    
    # We use a public model that is usually allowed
    image = client.text_to_image(prompt, model="stabilityai/stable-diffusion-2-1")
    return image
