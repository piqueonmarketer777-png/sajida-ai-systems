import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import urllib.parse

def generate_banner(prompt):
    try:
        encoded_prompt = urllib.parse.quote(prompt)
        api_url = f"https://image.pollinations.ai/p/{encoded_prompt}?model=flux"
        
        response = requests.get(api_url, timeout=30)
        
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            return image
        else:
            st.error("Could not generate image.")
            return None
    except Exception as e:
        st.error(f"Error: {e}")
        return None
