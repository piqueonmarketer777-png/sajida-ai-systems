#from st_paywall import add_auth
import streamlit as st
from generate import generate_banner

# Activate the paywall
add_auth(required=True)

# Set the page title
st.set_page_config(page_title="Sajida AI Systems")

# Title and Subheader
st.title("Sajida AI Systems - Image Generator")
st.subheader("Professional AI Visuals")

# Input field for the user to type their prompt
user_prompt = st.text_input("Enter your banner description:")

# Button to trigger the generation
if st.button("Generate Image"):
    if user_prompt:
        with st.spinner('Generating... please wait.'):
            image = generate_banner(user_prompt)
            if image:
                st.image(image, caption="Generated Banner")
                st.success("Success! Image created.")
                
                # Download button for the generated image
                st.download_button(
                    label="Download Image",
                    data=image,
                    file_name="generated_banner.png",
                    mime="image/png"
                )
    else:
        st.warning("Please enter a description first.")
