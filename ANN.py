import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tensorflow as tf

class ANN:
    def __init__(self, eta, epochs):
        pass

    def ann_model:
        LAYERS = [
            tf.keras.layers.Flatten(input_shape=[28, 28], name="inputLayer"),
            tf.keras.layers.Dense(300, activation="relu", name="hidden1"),
            tf.keras.layers.Dense(100, activation="relu", name="hidden2"),
            tf.keras.layers.Dense(10, activation="softmax", name="outputLayer")
        ]
        model_clf = tf.keras.models.Sequential(LAYERS)
        model_clf.layers



