# Installation

## Install Packages

```
pip3 install -r requirements.txt
```

## Download Model

By default, we are using [OpenLLaMA 7B](https://github.com/openlm-research/open_llama). Because we are using `llama.cpp` (with 4-bit quantization), models of this size can be used with relatively high speed, even on consumer hardware.

Another benefit of 4-bit quantization is the model size. The quantized 7B model is under 4 GB large, allowing for faster downloading.

To download the model, run the following script **from the base directory of this project**:

```
sh devtools/download-model.sh
```

Optionally, you can also load larger models.

## (Optional): Optimizations

### Apple Silicon

If you are using an Apple Silicon Mac, running the following (optional) script will drastically speed up your performance.

```
sh devtools/cpp-m1.sh
```