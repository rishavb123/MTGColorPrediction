import os
import tensorflow as tf
import time

from constants import LEARNING_RATE
from load_data import load_data
from model import ColorClassifier
from utils import time_func

s = str(int(time.time() * 1000))
log_dir = f"logs/tb/{s}"
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model = ColorClassifier()

X, y = time_func(load_data, "Loading data into memory . . .")

print(X.shape, y.shape)

optimizer = tf.keras.optimizers.Adam(LEARNING_RATE)
cross_entropy = tf.keras.losses.BinaryCrossentropy()

model.compile(optimizer=optimizer, loss=cross_entropy, metrics=['accuracy'])
model.fit(X, y, epochs=10, callbacks=[tensorboard_callback])

os.mkdir(f'./models/{s}')
model.save(f'models/{s}/model')