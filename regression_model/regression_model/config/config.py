# Import libraries 
from pathlib import Path
from strictyaml import load, Map, Str, Int, Seq, YAMLError

import regression_model

# Project Directories
PACKAGE_ROOT = Path(regression_model.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"

print(CONFIG_FILE_PATH)
# DATASET_DIR = PACKAGE_ROOT / "datasets"
# TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"

def fetch_yml_cofig_file():
    with open(f"{example.yaml}", 'r') as stream:
        try:
            return  load(conf_file.read())
        except YAMLError as exc:
            print(exc)

    return None
