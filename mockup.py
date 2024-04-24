import gradio as gr

# A placeholder function to return a fixed output
def mock_up(prompt, temperature, maximum_length, top_p):
    return "Hello, world!"


demo = gr.Interface(
    fn=mock_up,
    inputs=["text", "slider","slider","slider"],
    outputs=["text"],
)

demo.launch(share=True)
