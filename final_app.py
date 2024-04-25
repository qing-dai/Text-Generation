import gradio as gr

from transformers import pipeline, GenerationConfig

# Create a text generation pipeline
generator = pipeline("text-generation", model="gpt2")
config = GenerationConfig.from_pretrained("gpt2")


# config = GenerationConfig.from_pretrained("gpt2")

# The default config of GPT-2 is greedy decoding

# Generate text
# generator("Once upon a time, ", max_new_tokens=20, num_beams = 5)

def text_generate(prompt, temperature, maximum_length, top_p):
    # config max_length first
    config.max_new_tokens = maximum_length
    # depending on temp and top_p, we decide whether to use greedy_search or not
    if temperature == 0 or top_p == 0:
        config.do_sample = False
    else:
        config.do_sample = True
        config.temperature = temperature
        config.top_p = top_p
    generated_text = generator(prompt,
                               generation_config=config)
    return generated_text[0]["generated_text"]


# use actual class for gr.Textbox to have access to much more customizablility

demo = gr.Interface(
    fn=text_generate,
    inputs=[gr.Textbox(label="Prompt", value="Type in whatever you want to start with", lines=5),
            gr.Slider(label="Temperature", value=1, minimum=0, maximum=2,
                      info="Adjusts randomness in text generation; lower values produce "
                           "more predictable text, higher values encourage creativity and variety."),
            gr.Slider(label="Maximum_length", value=16, minimum=1, maximum=256, step=1,
                      info="Sets the upper limit on the text length, defining how many words the model will generate before stopping. "),
            gr.Slider(label="Top_p", value=1, minimum=0, maximum=1,
                      info="Filters the model’s choices to a set of high-probability options, "
                           "balancing between creativity and coherence in the text output.")],
    outputs=[gr.Textbox(label="Output", value="Hello, world!")],
)

demo.launch(share=True)
