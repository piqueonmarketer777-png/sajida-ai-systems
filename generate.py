from huggingface_hub import InferenceClient
import streamlit as st

def generate_banner(prompt):
    api_key = st.secrets["HUGGINGFACE_API_TOKEN"]
    # We create the client specifically for the model
    client = InferenceClient(model="runwayml/stable-diffusion-v1-5", token=api_key)
    
    # We use text_to_image directly on the client
    image = client.text_to_image(prompt)
    return image
