import gradio as gr
from openai import OpenAI

# Initialize the OpenAI client pointing to LM Studio
# LM Studio typically runs on localhost:1234 by default
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def predict(message, history):
    # Construct the chat history for the API
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})
    messages.append({"role": "user", "content": message})

    # Call the model
    response = client.chat.completions.create(
        model="google/gemma-4-e4b", # Adjust model name if needed
        messages=messages,
        temperature=0.7,
        stream=True
    )

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            partial_message += chunk.choices[0].delta.content
            yield partial_message

# Define an old-fashioned CSS theme
# Using "retro" colors: beige/green/monospaced fonts
css = """
body { background-color: #f0e6d2 !important; font-family: 'Courier New', Courier, monospace !important; }
.gradio-container { border: 2px solid #555; background-color: #fdf6e3 !important; }
h1 { color: #333; text-transform: uppercase; border-bottom: 2px solid #333; }
.message { font-family: 'Courier New', Courier, monospace !important; border: 1px solid #ccc !important; }
"""

# Build the Gradio interface
demo = gr.ChatInterface(
    predict,
    title="TERMINAL-CHAT-V1.0",
    description="Gemma-4-e4b via LM Studio Gateway. Authenticated: [OK].",
    css=css,
    theme=gr.themes.Monochrome()
)

if __name__ == "__main__":
    demo.launch()
