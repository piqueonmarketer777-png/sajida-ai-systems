import streamlit as st
from generate import generate_banner

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
            # This calls the function we prepared in generate.py
            generate_banner(user_prompt)
            
            # Display the generated image
            st.image("banner.png", caption="Generated Banner")
            st.success("Success! 'banner.png' has been created.")
        
        # New code added here:
        with open("banner.png", "rb") as file:
            st.download_button(
                label="Download Image",
                data=file,
                file_name="banner.png",
                mime="image/png"
            )
    else:
        st.warning("Please enter a description first.")