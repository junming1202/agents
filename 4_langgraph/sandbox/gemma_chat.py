import gradio as gr
from openai import OpenAI

# Initialize the OpenAI client pointing to LM Studio
# By default, LM Studio runs on port 1234
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def chat_function(message, history):
    messages = []
    
    # Format history for OpenAI API
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})
    
    messages.append({"role": "user", "content": message})
    
    response = client.chat.completions.create(
        model="google/gemma-4-e4b",
        messages=messages,
        temperature=0.7,
        stream=True
    )
    
    partial_text = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            partial_text += chunk.choices[0].delta.content
            yield partial_text

# Create the Gradio interface with an "old-fashioned" styling theme
# Using classic 'monochrome' or just CSS tweaks to simulate 90s aesthetic
css = """
body {
    background-color: #c0c0c0 !important;
    font-family: 'Courier New', Courier, monospace !important;
}
.gradio-container {
    border: 2px outset white !important;
    background-color: #c0c0c0 !important;
}
button {
    background-color: #c0c0c0 !important;
    border: 2px outset white !important;
    font-weight: bold !important;
}
input, textarea {
    background-color: white !important;
    border: 2px inset gray !important;
}
"""

demo = gr.ChatInterface(
    fn=chat_function,
    title="Gemma Terminal Interface",
    description="Connection to LM Studio - legacy mode enabled.",
    theme=gr.themes.Base(),
    css=css
)

if __name__ == "__main__":
    demo.launch()
