import streamlit as st
from generate import generate_banner
st.set_page_config(page_title="Sajida AI Systems")
st.title("Sajida AI Systems -  Image Geneartor")
st.subheader("Professional  AI Visuals")
user_prompt = st.text_input("Entre your banner description:")
if st.button("Generate Image"):
    if user_prompt:
        with st.spinner('Generating...please wait.'):
            image = genearte_banner(user_prompt)
            if image:
                st.image(image, caption="Generated Banner")
                st.success("Success! Image created.")
                st.download_button(
                    label="Download Image",
                    data=image,
                    file_name="generated_banner.png",
                    mime="image/png"
                )
    else:
        st.warning
                
