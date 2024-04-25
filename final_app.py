import gradio as gr

from transformers import pipeline, GenerationConfig,  PhrasalConstraint

# Create a text generation pipeline
generator = pipeline("text-generation", model="gpt2")
config = GenerationConfig.from_pretrained("gpt2")

# The default config of GPT-2 is greedy decoding


def text_generate(prompt, temperature, maximum_length, top_p, num_beams=3, force_word=None):
    # config max_length first
    config.max_new_tokens = maximum_length
    # Add force_word option for output
    if force_word:
        config.do_sample = False
        force_word_id = generator.tokenizer(force_word, add_special_tokens=False).input_ids
        constraints = [
            PhrasalConstraint(force_word_id),
        ]
        generated_text = generator(prompt, num_beams=num_beams if num_beams > 1 else 3,
                                   generation_config=config,
                                   constraints=constraints)
        print(f"I am using force model")
    # depending on temp and top_p, we decide whether to use greedy_search or not
    elif temperature == 0 or top_p == 0:
        config.do_sample = False
        generated_text = generator(prompt,
                                   generation_config=config)
        print("I am using 0 model")
    else:
        config.do_sample = True
        config.temperature = temperature
        config.top_p = top_p
        generated_text = generator(prompt,
                                   generation_config=config)
        print("I am using top_p model")

    print(config.do_sample)

    return generated_text[0]["generated_text"]



# use actual class for gr.Textbox to have access to much more customizablility

demo = gr.Interface(
    fn=text_generate,
    # Allow users to select pre-defined prompts from dropdowns
    inputs=[gr.Dropdown(['Today is Christmas, ',
                        "Type in whatever you want to start with",
                        "Let's go party, "],
                        label="Prompt",
                       value="Type in whatever you want to start with"
                       ),
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
