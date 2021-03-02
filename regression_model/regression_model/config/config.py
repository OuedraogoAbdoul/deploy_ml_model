# Import libraries 
from pathlib import Path

# Get main folder path
ROOT = f"{Path(__file__).resolve().parents[2]}"
ROOT = ROOT.split("/")[-1]

## Data path
SYMBOLS = "BTC-USD"

DATAFILE = "BTC-USD.csv"
DATA = ROOT + "/data/" + DATAFILE
TRAININGDATA = ROOT + "/data/" + "train.csv"
TESTINGDATA = ROOT + "/data/" + "test.csv"
WRONGDATAPATH = 999

#####prediction feature

TARGER = ""


### Features

FEATURES = [""]
