import tensorflow as tf

class ColorClassifier(tf.keras.Model):

    def __init__(self) -> None:
        super(ColorClassifier, self).__init__()
        self.layers = [
            tf.keras.layers.Conv2D(64, strides=(5, 5), input_shape=(156, 114, 3)), # (152, 110, 64)
            tf.keras.layers.LeakyReLU(),
            tf.keras.layers.MaxPooling2D((2, 2)), # (76,  55, 64)
            tf.keras.layers.Dropout(0.3),

            tf.keras.layers.Conv2D(128, strides=(3, 3)), # (74, 53, 128)
            tf.keras.layers.MaxPooling2D((2, 2)), # (37, 26, 128)
            tf.keras.layers.Dropout(0.3),

            tf.keras.layers.Conv2D(128, strides=(2, 2)), # (36, 25, 128)
            tf.keras.layers.MaxPooling2D((2, 2)), # (18, 12, 128)
            tf.keras.layers.Dropout(0.3),

            tf.keras.layers.Flatten(), # (18*12*128)

            tf.keras.layers.Dense(2000, activation='relu'),
            tf.keras.layers.Dropout(0.3),

            tf.keras.layers.Dense(1000, activation='relu'),
            tf.keras.layers.Dropout(0.3),
            
            tf.keras.layers.Dense(500, activation='relu'),
            tf.keras.layers.Dropout(0.3),
            
            tf.keras.layers.Dense(5, activation='sigmoid')
        ]
        
    def call(self, inputs, training=False):
        x = inputs
        for layer in self.layers:
            if not isinstance(layer, tf.keras.layers.Dropout):
                x = layer(x)
            else:
                x = layer(x, training=training)
        return x

