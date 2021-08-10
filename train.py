from timer import time_func
from load_data import load_data
from model import ColorClassifier

# model = ColorClassifier()

X, y = time_func(load_data, "Loading data into memory . . .")