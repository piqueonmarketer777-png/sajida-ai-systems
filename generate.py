import requests
import streamlit as st
import io
from PIL import Image

def generate_banner(prompt):
    api_key = st.secrets["HUGGINGFACE_API_TOKEN"]
    # Using the primary Inference API endpoint
    api_url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    try:
        # We perform a POST request
        response = requests.post(api_url, headers=headers, json={"inputs": prompt}, timeout=60)
        
        if response.status_code == 200:
            return Image.open(io.BytesIO(response.content))
        else:
            # If the model is still loading, it returns 503
            if response.status_code == 503:
                st.warning("Model is currently loading. Please wait a moment and try again.")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error("A network error occurred. Please try again in a moment.")
        return None
