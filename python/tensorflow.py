# Tensorflow-related tips

# Choosing only one GPU
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
os.environ["CUDA_VISIBLE_DEVICES"]="0,1"

# Using a fraction of the GPU:
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
