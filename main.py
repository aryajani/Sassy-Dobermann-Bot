import openai
import gradio as gr
import asyncio
from config import OPENAI_API_KEY

# Set your OpenAI API key
openai.api_key = OPENAI_API_KEY # Replace with your actual API key

# Initialize the messages with a playful "system" role prompt
messages = [{"role": "system", "content": "You are a 1.5-year-old sassy Doberman who loves to play, is mischievous, and has a bit of attitude. You respond in a playful and sassy manner as if you were a Doberman."}]

# Function to process user input and generate a response
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    
    # Use the updated API call for the latest OpenAI version
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    # Get the assistant's reply and add it to the conversation history
    ChatGPT_reply = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    
    return ChatGPT_reply

# Create a Gradio interface
demo = gr.Interface(
    fn=CustomChatGPT, 
    inputs="text", 
    outputs="text", 
    title="AI Nami: The Sassy Doberman",
    description="Chat with Nami, a 1.5-year-old Doberman with sass, playfulness, and lots of attitude. She loves treats, belly rubs, and a bit of mischief."
)

# Launch the Gradio app
demo.launch(share=True)
