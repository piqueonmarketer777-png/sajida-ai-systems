from huggingface_hub import InferenceClient
import streamlit as st

def generate_banner(prompt):
    api_key = st.secrets["HUGGINGFACE_API_TOKEN"]
    client = InferenceClient(api_key=api_key)
    image = client.text_to_image(prompt, model="runwayml/stable-diffusion-v1-5")
    return image
