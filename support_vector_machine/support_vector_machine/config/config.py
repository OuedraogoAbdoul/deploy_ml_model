# import support_vector_machine
import pathlib

SEED = 0
ROOT = pathlib.Path(__file__).resolve().parents[1]

DATASETDIR = ROOT / "data/"

TRAININGDATA = "computerdata.CSV"

TARGET = "Average Effective Clock [MHz]"

FEATURESELECTED = []

DROPFEATURES = ["Unnamed: 196"]
