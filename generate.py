import streamlit as st
from huggingface_hub import InferenceClient

def generate_banner(prompt):
    try:
        api_key = st.secrets["HUGGINGFACE_API_TOKEN"]
        client = InferenceClient(api_key=api_key)
        # Using a more stable model ID
        image = client.text_to_image(prompt, model="runwayml/stable-diffusion-v1-5")
        return image
    except Exception as e:
        st.error(f"Hugging Face is currently busy or the model is unavailable. Please try again in a moment. (Error: {e})")
        return None
