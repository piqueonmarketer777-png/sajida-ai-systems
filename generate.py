import streamlit as st
import torch
from diffusers import StableDiffusionPipeline

def generate_banner(prompt):
    try:
        # Load the stable diffusion model
        model_id = "runwayml/stable-diffusion-v1-5"
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id, 
            torch_dtype=torch.float32
        )
        
        # Move to CPU since free spaces usually don't have GPUs
        pipe = pipe.to("cpu")
        
        # Generate the image
        image = pipe(prompt).images[0]
        return image
    except Exception as e:
        st.error(f"Generation error: {e}")
        return None
