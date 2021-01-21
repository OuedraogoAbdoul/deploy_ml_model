# import support_vector_machine
import pathlib

SEED = 0
VERSION = "0.0.1"
MODEL_NAME = "SVR"


ROOT = pathlib.Path(__file__).resolve().parents[1]

DATASETDIR = ROOT / "data/"

X_test = "X_test.csv"
y_test = "y_test.csv"

TRAININGDATA = "computerdata.csv"

TESTDATA = "test.csv"


TARGET = "Average Effective Clock [MHz]"

FEATURESELECTED = []

DROPFEATURES = ["Unnamed: 196"]

MODEL_SAVE_PATH =  ROOT / "trainded_model"

MODEL_SAVE_FILE = f"{MODEL_NAME}_{VERSION}"
