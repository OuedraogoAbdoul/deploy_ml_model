from support_vector_machine.config import config
import pandas as pd
import numpy as np
import joblib


def load_dataset(file_name):
    """

    """
    _dataset = pd.read_csv(f"{config.DATASETDIR}/{file_name}")
    return _dataset


def save_model(*, save_model):
    save_file_name = f"{config.MODEL_NAME}_{config.VERSION}.pkl"
    save_path = config.MODEL_SAVE_PATH / save_file_name

    joblib.dump(save_model, save_path)


def load_model():
    model_name  = f"{config.MODEL_NAME}_{config.VERSION}.pkl"
    svr_model = joblib.load(config.MODEL_SAVE_PATH/model_name)
    return svr_model


def remove_saved_models():
    pass
