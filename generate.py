from huggingface_hub import InferenceClient
import streamlit as st

def generate_banner(prompt):
    api_key = st.secrets["HUGGINGFACE_API_TOKEN"]
    # We initialize the client to use the specific Inference API URL
    client = InferenceClient(model="runwayml/stable-diffusion-v1-5", token=api_key)
    
    # We use the task-specific call which is more stable
    image = client.text_to_image(prompt)
    return image
