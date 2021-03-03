from regression_model.config import config
from sklearn.pipeline import Pipeline
from regression_model.get_data import read_data
from regression_model.preprosessing import data_preprocessors as pp


btc_price_pipeline = Pipeline(
    [
        (
            "split into train test",
            pp.SplitTrainTest(variables=read_data()),
        )
    ]
)