# Import libraries 
from pathlib import Path

# Get main folder path
ROOT = f"{Path(__file__).resolve().parents[2]}"
ROOT = ROOT.split("/")[-1]

## Data path
SYMBOLS = "BTC-USD"
DATASETS = ROOT + "/data/"
X_train = DATASETS + "X_train.csv"
y_train = DATASETS + "y_train.csv"


X_test = DATASETS + "X_test.csv"
y_test = DATASETS + "y_test.csv"


DATAFILE = "BTC-USD.csv"
DATA = DATASETS + DATAFILE
TRAININGDATA = DATASETS + "train.csv"
TESTINGDATA = DATASETS + "test.csv"
WRONGDATAPATH = 999

#####prediction feature

TARGER = "Open"


### Features

FEATURES = [""]
