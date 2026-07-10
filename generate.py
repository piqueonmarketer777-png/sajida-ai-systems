import streamlit as st
from huggingface_hub import InferenceClient

# Retrieve the key from Streamlit Secrets
api_key = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

# Pass the key to the client
client = InferenceClient(api_key=api_key)

def generate_banner(prompt):
    # Now this will work because 'client' has the key
    image = client.text_to_image(prompt, model="black-forest-labs/FLUX.1-schnell")
    return image
