from src.utils.common import read_config
from src.utils.data_mgmt import get_data
from src.utils.model import create_model
import os
import argparse

def training(config_path):
    config = read_config(config_path)
    validation_datasize = config["params"]["validation_datasize"]
    (X_train, y_train), (X_valid, y_valid), (X_test,y_test) = get_data(validation_datasize)

    LOSS = config["params"]["loss_fucntion"]
    OPTIMIZER = config["params"]["optimizer"]
    METRICS = config["params"]["metrics"]
    NUM_CLASSES = config["params"]["num_classes"]

    model = create_model(LOSS, OPTIMIZER, METRICS, NUM_CLASSES)

    EPOCHS = config["params"]["epochs"]
    VALIDATION_SET = (X_valid, y_valid)

    history = model.fit(X_train, y_train, epochs=EPOCHS,
                        validation_data = VALIDATION_SET)

    artifacts_dir = config["artifacts"]["artifacts_dir"]
    model_dir = config["artifacts"]["model_dir"]

    model_dir_path = os.join.path(artifacts_dir, model_dir)
    os.mkdirs(model_dir_path, exists_ok=True)
    model_name = config["artifacts"]["model_name"]
    save_model(model, model_name, model_dir)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default = "config.yml")
    parsed_args = args.parse_args()
    training(config_path = parsed_args.config)