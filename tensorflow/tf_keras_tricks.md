## Tensorflow / Keras steps for model reproducibility

### CPU:
---

1. Initializing model weights:

```
k_init = tf.keras.initializers.RandomUniform(seed=8)
layer =  tensorflow.keras.layers.Dense(kernel_initializer=k_init)
```

2. Customize shuffle during model.fit():

```
train_df = train_df.shuffle(len(train_df), random_state=8)
model.fit(train_df[x_cols], train_df[y_cols], shuffle=False)
```

3. If using numpy array, use np.random.shuffle(ar)

4. If using cross-validation:

```
kf = sklearn.model_selection.KFold(random_state=8)
for i_k_1, i_1 in kf.split(data.index):
    train_data = data.loc[data.index[i_k_1], :]
    train_data = train_data.sample(len(train_data), random_state=8)
    cv_data = data.loc[data.index[i_1], :]
    cv_data = cv_data.sample(len(cv_data), random_state=8)
```

### GPU:
---

- If using `tensorflow=2.1.0` (onward?), reproducibility is guaranteed as these lines below are already running
- Ref [NVIDIA Patch](https://github.com/NVIDIA/tensorflow-determinism). 

```
import tensorflow as tf
import os
os.environ['TF_DETERMINISTIC_OPS'] = '1'
# Now build your graph and train it
```

- If using `tensorflow < 2.1`, follow instructions [on same link](https://github.com/NVIDIA/tensorflow-determinism).
```
from tfdeterminism import patch
patch()
```

## Ignore Tensorflow warning(s):

```
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```
- 0 (default): displaying all logs
- 1: filter out INFO logs
- 2: additionally filter out WARNINGS
- 3: filter out ERROR logs
