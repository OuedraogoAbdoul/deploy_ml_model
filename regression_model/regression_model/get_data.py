import pandas as pd
from sklearn.model_selection import train_test_split
from regression_model.config import config

from regression_model.config.config import SYMBOLS, ROOT, DATA


def read_data(symbols="BTC-USD"):
    ###Use if the data is read from online resources
    # if(isinstance(symbols, str)):
    #     data = data.DataReader(symbols, start="2014-15-09", end=today)
    # else:
    #     data = data.DataReader(f"{symbols}", start="2017-01-01", end=today)

    # Line for already downloaded data
    data = pd.read_csv(DATA)
    X = data.loc[:, data.columns != config.TARGER]
    y = data.pop(config.TARGER)
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
    data_features = list(X_train.columns)
    pd.DataFrame(X_train, columns=data_features).to_csv(config.X_train, index=False)
    pd.DataFrame(y_train, columns=data_features).to_csv(config.y_train, index=False)

    pd.DataFrame(X_test, columns=data_features).to_csv(config.X_test, index=False)
    pd.DataFrame(y_test, columns=data_features).to_csv(config.y_test, index=False)

    return data

if __name__ == "__main__":
    df = read_data()
    print("Data splitting completed: ", df.head())