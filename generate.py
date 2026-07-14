from huggingface_hub import InferenceClient
import streamlit as st

def generate_banner(prompt):
    # Retrieve the key from Streamlit Secrets
    api_key = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
    client = InferenceClient(api_key=api_key)
    
    # Generate the image
   # Change from FLUX.1-schnell to this:
image = client.text_to_image(prompt, model="stabilityai/stable-diffusion-2-1")
    
    # IMPORTANT: You must return the image!
    return image
