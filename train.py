import os
import tensorflow as tf
import time

from constants import LEARNING_RATE
from load_data import load_data
from model import ColorClassifier
from utils import time_func

model = ColorClassifier()

X, y = time_func(load_data, "Loading data into memory . . .")

print(X.shape, y.shape)

optimizer = tf.keras.optimizers.Adam(LEARNING_RATE)
cross_entropy = tf.keras.losses.BinaryCrossentropy()

model.compile(optimizer=optimizer, loss=cross_entropy, metrics=['accuracy'])
model.fit(X, y, epochs=10)

s = str(int(time.time() * 1000))
os.mkdir(f'./models/{s}')
model.save(f'models/{s}/model')