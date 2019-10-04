# Tensorflow-related tips

# Choosing only one GPU
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
os.environ["CUDA_VISIBLE_DEVICES"]="0,1"