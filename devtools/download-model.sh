#!/bin/bash
rm -rf models
mkdir models
# url="https://huggingface.co/clearmindai/open-llama-7b-ggml-mirror/resolve/main/ggml-model-q4_0.bin"
url="https://huggingface.co/clearmindai/open-llama-7b-ggml-mirror/resolve/main/ggml-model-q4_1.bin"
directory="models"
echo "Checking if wget is available"
if command -v wget >/dev/null 2>&1; then
    echo "Using wget"
    wget -P "$directory" "$url"
else
    if command -v curl >/dev/null 2>&1; then
    echo "wget is unavailable. Checking if curl is available"
        echo "Using curl"
        curl -o "$directory" "$url"
    else
        echo "Error: Neither wget nor curl is installed. Please install either of them."
        exit 1
    fi
fi

echo "Model downloaded successfully to $directory/$filename."
