from support_vector_machine.config import config
import pandas as pd
import numpy as np



def load_dataset(file_name):
    """

    """
    _dataset = pd.read_csv(f"{config.DATASETDIR}/{file_name}")
    return _dataset


def save_model():
    pass



def load_model():
    pass


def remove_saved_models():
    pass
