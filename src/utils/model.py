import tensorflow as tf
import time
import os

def create_model(LOSS, OPTIMIZER, METRICS, NUM_CLASSES):
    LAYERS = [
        tf.keras.layers.Flatten(input_shape=[28, 28], name="inputLayer"),
        tf.keras.layers.Dense(300, activation="relu", name="hidden1"),
        tf.keras.layers.Dense(100, activation="relu", name="hidden2"),
        tf.keras.layers.Dense(NUM_CLASSES, activation="softmax", name="outputLayer")
    ]

    model_clf = tf.keras.models.Sequential(LAYERS)
    LOSS = "sparse_categorical_crossentropy"
    OPTIMIZER = "SGD"
    METRICS = ["accuracy"]

    model_clf.summary()

    model_clf.compile(loss=LOSS, optimizer=OPTIMIZER, metrics=METRICS)

    return model_clf ##untrained model

def get_unique_filename(filename):
    unique_filename = time.strftime(f"%Y%m%d_%H%M%S_{filename}")

def save_model(model, model_name, model_dir):
    unique_name = get_unique_filename(model_name)
    path_to_model = os.path.join(model_dir, unique_name)
    model.save(path_to_model)

