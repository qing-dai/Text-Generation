# Text Generation Demo with GPT-2

This project implements a web-based interface for generating 
text using OpenAI's GPT-2 model, similar to the **OpenAI Play-ground**.  It allows users to interactively
customize the generation process by setting various parameters 
such as temperature, maximum length, and others.

## Features

- **Customizable Text Generation**: Users can specify the starting prompt, adjust the temperature for randomness, set the maximum length of the generated text, and control the probability threshold for token selection.
- **Beam Search**: Users can adjust the number of beams used in the beam search process to explore different paths in generating text.
- **Force Word Inclusion**: An optional feature to include a specified word in the generated text, enhancing the relevance of the output to user-specified constraints.

## Setup

### Requirements

- Python 3.7+
- Gradio
- Transformers

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/qing-dai/Text-Generation.git
   cd Text_Generation
   
2. **Install dependencies**

It is recommended to create a virtual environment for Python projects to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

```

3. **Running the Application**

Run the application with the following command:
```bash
python final_app.py
```

This will start a local server, and you can interact with the demo by navigating to the URL provided by Gradio in your web browser.

### How to Use
- **Select a prompt** from the dropdown menu or type your own to start the text generation.
- **Adjust the Temperature** slider to set the randomness level of text generation.
- **Set the Maximum Length** for the generated text using the slider.
- **Adjust the Top_p** slider to filter the choices based on the cumulative probability.
- **Set the Number of Beams** for the beam search.
- **Optionally, enter a word** in the "Force Word" textbox that you want to appear in the generated text.

##### After setting the desired parameters, click the "Submit" button to generate the text. The generated text will appear in the output box below the interface controls.

### License
This project is open-sourced under the MIT License. See the LICENSE file for more details.

### Author
Qing Dai (qing.dai@uzh.ch)
Feel free to open an issue or send a pull request if you have suggestions or contributions to the code.

