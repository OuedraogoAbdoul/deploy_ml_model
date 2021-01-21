from sklearn.preprocessing import OneHotEncoder
from support_vector_machine.config import config

from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from support_vector_machine.preprocessing.data_manager import load_dataset, save_model, load_model
import pandas as pd

def validate_input_data(test_data):

    full_test_data = pd.read_csv(f"{config.DATASETDIR}/{test_data}")

    y = full_test_data[config.TARGET]
    X = full_test_data.loc[:, full_test_data.columns != config.TARGET]
    X = pd.get_dummies(X)

    scaler = MinMaxScaler()
    X = pd.DataFrame(scaler.fit_transform(X))

    return X, y
