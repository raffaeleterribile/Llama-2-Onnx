I've had to install CUDA 11.8 vefore installing suggested requirements:

conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia

After that, I've installed the requirements:

pip install torch onnxruntime-gpu numpy sentencepiece

Installing CUDA 12, torchvision or torchaudio gives strange errors
