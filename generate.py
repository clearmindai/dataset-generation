import os
import sys
from llama_cpp import Llama
from tqdm import tqdm
import random

def suppress_output():
    sys.stdout = open(os.devnull, 'w')
def restore_output():
    sys.stdout = sys.__stdout__

if not os.path.isfile('models/ggml-model-q4_1.bin'):
    print("Oops! It looks like you haven't downloaded the model yet! Please run `devtools/download-model.sh` **from the base directory of this project** to download the models or see INSTALLATION.md for detailed instructions.")
    sys.exit(0)

if not os.path.exists('data'):
    os.makedirs('data')

# llm = Llama(model_path="models/ggml-model-q4_1.bin")
llm = Llama(model_path="models/open-llama-3b-q4_1.bin")
# llm = Llama(model_path="models/llama-13b-q4_1.bin")
for number in tqdm(range(0, 10000)):
    file_path = f"data/data_{number}.txt"
    llm.seed = random.randint(1, 1000)
    with open('prompt.txt', 'r') as f:
        prompt = f.read()
    # output = llm(prompt, max_tokens=2048, stop=["\n"], echo=False)
    output = llm(prompt, max_tokens=1024, echo=False)
    text = output['choices'][0]['text']
    with open(file_path, 'w') as file:
        file.write(text)
    tqdm.write(f"Dataset data #{number} created.")

print("Dataset generated!")