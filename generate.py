import streamlit as st
import torch
from diffusers import StableDiffusionPipeline

def generate_banner(prompt):
    try:
        # Load the model with optimizations for low-memory environments
        model_id = "runwayml/stable-diffusion-v1-5"
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id, 
            torch_dtype=torch.float32,
            low_cpu_mem_usage=True # Add this optimization
        )
        
        # Explicitly move to CPU
        pipe = pipe.to("cpu")
        
        # Generate the image
        image = pipe(prompt).images[0]
        return image
    except Exception as e:
        st.error(f"Generation error: {e}")
        return None
