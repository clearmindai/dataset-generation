import os
import sys
if not os.path.isfile('models/ggml-model-q4_0.bin'):
    print("Oops! It looks like you haven't downloaded the model yet! Please run `devtools/download-model.sh` **from the base directory of this project** to download the models or see INSTALLATION.md for detailed instructions.")
    sys.exit(0)