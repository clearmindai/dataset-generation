echo "Optimizing llama-cpp-python for M1"
echo "If you don't have an M1, you can reverse these changes by running: 'pip uninstall llama-cpp-python' and then 'pip install llama-cpp-python'"
pip uninstall llama-cpp-python -y
CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install -U llama-cpp-python --no-cache-dir
pip install 'llama-cpp-python[server]'
echo "Done"