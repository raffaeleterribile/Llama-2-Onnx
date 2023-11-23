I've had to install CUDA 11.8 vefore installing suggested requirements:

conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia

After that, I've installed the requirements:

pip install torch onnxruntime-gpu numpy sentencepiece

Installing CUDA 12, torchvision or torchaudio gives strange errors

I've got problems with GPU memory: it's too small

I've succeded loading model on CPU with this configuration:

conda install pytorch -c pytorch
pip install torch onnxruntime numpy sentencepiece
