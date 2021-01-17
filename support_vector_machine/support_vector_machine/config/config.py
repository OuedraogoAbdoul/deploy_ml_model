# import support_vector_machine
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

MAINDATASET = ROOT / "data/computerdata.CSV"

TARGET = "Average Effective Clock [MHz]"
FEATURESELECTED = []

DROPFEATURES = ["Unnamed: 196"

]
