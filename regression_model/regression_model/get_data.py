import pandas as pd
from regression_model.config.config import SYMBOLS, ROOT, DATA


def read_data(symbols="BTC-USD"):
    ###Use if the data is read from online resources
    # if(isinstance(symbols, str)):
    #     data = data.DataReader(symbols, start="2014-15-09", end=today)
    # else:
    #     data = data.DataReader(f"{symbols}", start="2017-01-01", end=today)

    # Line for already downloaded data
    data = pd.read_csv(DATA)

    return data

if __name__ == "__main__":
    df = read_data()
    print(df.head())