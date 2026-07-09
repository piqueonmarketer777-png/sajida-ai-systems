from huggingface_hub import InferenceClient
import os
client = InferenceClient(token=os.environ.get("HUGGINGFACE_TOKEN"))

# Change: Add 'prompt' as an argument here
def generate_banner(prompt):
    print("Generating... please wait.")
    image = client.text_to_image(prompt, model="black-forest-labs/FLUX.1-schnell")
    image.save("banner.png")
    print("Success! 'banner.png' has been created.")

if __name__ == "__main__":
    # This part only runs if you run this file directly in terminal
    user_prompt = input("Enter your banner description: ")
    generate_banner(user_prompt)
