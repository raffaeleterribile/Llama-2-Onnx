# Requirements
I've had to install CUDA 11.8 vefore installing suggested requirements:

conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia

After that, I've installed the requirements:

pip install torch onnxruntime-gpu numpy sentencepiece

Installing CUDA 12, torchvision or torchaudio gives strange errors

I've got problems with GPU memory: it's too small

I've succeded loading model on CPU with this configuration:

conda install pytorch -c pytorch
pip install torch onnxruntime numpy sentencepiece

# Performance test of the minimum example with the suggested parameters

.\test_duration.ps1

sabato 25 novembre 2023 10:41:04
...\onnxruntime_inference_collection.py:69: UserWarning: Specified provider 'DmlExecutionProvider' is not in available provider names.Available providers: 'AzureExecutionProvider, CPUExecutionProvider'
  warnings.warn(
---\onnxruntime_inference_collection.py:69: UserWarning: Specified provider 'CUDAExecutionProvider' is not in available provider names.Available providers: 'AzureExecutionProvider, CPUExecutionProvider'
  warnings.warn(


The lightest element is hydrogen. Hydrogen is the lightest element on the periodic table, with an atomic mass of 1.00794 u (unified atomic mass units).
sabato 25 novembre 2023 15:30:03
