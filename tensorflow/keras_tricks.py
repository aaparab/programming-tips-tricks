##############################
# Keras steps for model 
# reproducibility:
##############################

# 1. Initializing model weights:

k_init = tf.keras.initializers.RandomUniform(seed=8)
layer =  tensorflow.keras.layers.Dense(kernel_initializer=k_init)

# 2. Customize shuffle during model.fit():

train_df = train_df.shuffle(len(train_df), random_state=8)
model.fit(train_df[x_cols], train_df[y_cols], shuffle=False)

# If using numpy array, use np.random.shuffle(ar)

# 3. If using cross-validation:

kf = sklearn.model_selection.KFold(random_state=8)
for i_k_1, i_1 in kf.split(data.index):
    train_data = data.loc[data.index[i_k_1], :]
    train_data = train_data.sample(len(train_data), random_state=8)
    cv_data = data.loc[data.index[i_1], :]
    cv_data = cv_data.sample(len(cv_data), random_state=8)
