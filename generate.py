import requests
import streamlit as st
import io
from PIL import Image

def generate_banner(prompt):
    api_key = st.secrets["HUGGINGFACE_API_TOKEN"]
    api_url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    # We add a timeout of 60 seconds to allow the model time to load
    try:
        response = requests.post(api_url, headers=headers, json={"inputs": prompt}, timeout=60)
        
        if response.status_code == 200:
            return Image.open(io.BytesIO(response.content))
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")
        return None
