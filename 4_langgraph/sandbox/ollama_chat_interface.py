import gradio as gr
from openai import OpenAI
import os

# --- Configuration ---
# Ollama typically serves an OpenAI-compatible API endpoint at localhost:11434/v1
OLLAMA_API_BASE = "http://localhost:1234/v1"
MODEL_NAME = "google/gemma-4-e4b"

def generate_response(message, history):
    """
    Calls the Ollama API endpoint to get a response from the specified model.
    Uses an OpenAI-compatible client structure.
    
    Args:
        message (str): The current user message.
        history (list[tuple]): Chat history provided by Gradio.
    
    Returns:
        str: The model's response text.
    """
    print(f"Sending request to {MODEL_NAME}...")

    try:
        # Initialize the OpenAI client pointing to the local Ollama endpoint
        client = OpenAI(api_key="ollama", base_url=OLLAMA_API_BASE)

        # The history format expected by ChatCompletion is a list of dictionaries,
        # but for simplicity and stability with Gradio/OpenAI wrapper, we'll construct 
        # the message payload using the conversation turns.
        messages = []
        for user_message, bot_message in history:
            messages.append({"role": "user", "content": user_message})
            messages.append({"role": "assistant", "content": bot_message})

        # Add the current message
        messages.append({"role": "user", "content": message})
        
        # --- API Call ---
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7 # A good balance for chat
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"An error occurred: {e}")
        return f"Error communicating with the Ollama server or API endpoint. Please ensure 'ollama run {MODEL_NAME}' is running and accessible at {OLLAMA_API_BASE}. Error details: {e}"

# --- Gradio Interface Setup ---

# Custom CSS for an "old-fashioned" look
OLD_FASHIONED_CSS = """
body {
    background-color: #f0e6d8; /* Sepia background */
    font-family: 'Georgia', serif; /* Classic serif font */
}
.gradio-container {
    max-width: 700px;
    border: 15px solid #c2b280; /* Darker, ornate border (e.g., Tan/Khaki) */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth */
    background-color: #fffaf0; /* Off-white page color */
}
h1 {
    color: #6b5d3c; /* Deep brown text */
    text-align: center;
    border-bottom: 2px solid #a09278;
    padding-bottom: 10px;
}
.gradio-textbox, .gradio-button {
    background-color: #e6e0d4; /* Slightly darker input/button background */
    border: 1px solid #b5a392;
    transition: all 0.2s ease-in-out;
}
/* Hover effect for buttons to feel more tactile */
.gradio-button:hover {
    background-color: #d4c8bf;
    transform: translateY(-1px);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}
"""

# Create the chat interface
chat_interface = gr.ChatInterface(
    fn=generate_response,
    chatbot=gr.Markdown("Welcome to your Chat Interface.\n\n*Note: Please ensure that the Ollama model (`{MODEL_NAME}`) is running locally.*"), # Initial message styling
    textbox=gr.Textbox(placeholder="Enter your query here...", show_label=False),
    title="📜 The Grand Digital Scriptorium 🖋️", # Old-fashioned title
    description="A communication portal powered by the Gemma 4 model via Ollama's OpenAI compatible API.",
    # theme="soft" # Using a base theme and overriding with CSS
)

# Apply custom styling
chat_interface.css = OLD_FASHIONED_CSS

if __name__ == "__main__":
    print("Starting Gradio Interface...")
    # Launching the interface on local host
    chat_interface.launch()