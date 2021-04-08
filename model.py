import tensorflow as tf

class ColorClassifier(tf.keras.Model):

    def __init__(self) -> None:
        super(ColorClassifier, self).__init__()
        
    def call(self, inputs, training=False):
        return None

