import gradio as gr

# A placeholder function to return a fixed output
def mock_up(prompt, temperature, maximum_length, top_p):
    return "Hello, world!"

# use actual class for gr.Textbox to have access to much more customizablility

demo = gr.Interface(
    fn=mock_up,
    inputs=[gr.Textbox(label="Prompt",value="Type in whatever you want to start with",lines=5),
            gr.Slider(label="Temperature",value=1, minimum=0, maximum=2,
                      info="Adjusts randomness in text generation; lower values produce "
                           "more predictable text, higher values encourage creativity and variety."),
            gr.Slider(label="Maximum_length",value=16, minimum=1, maximum=256, step=1,
                      info="Sets the upper limit on the text length, defining how many words the model will generate before stopping. "),
            gr.Slider(label="Top_p",value=1, minimum=0, maximum=1,
                      info="Filters the model’s choices to a set of high-probability options, "
                           "balancing between creativity and coherence in the text output.")],
    outputs=[gr.Textbox(label="Output", value="Hello, world!")],
)

demo.launch(share=True)
