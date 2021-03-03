from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, TransformerMixin
from regression_model.get_data import read_data
import pandas as pd
from regression_model.config.config import X_TRAIN

class SplitTrainTest(BaseEstimator, TransformerMixin):
    """Split data into train and test"""

    def __init__(self, variables=pd.DataFrame) -> None:
        self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        """Fit template."""

        return self

    def transform(self, X: pd.DataFrame):
        """Apply the transforms to the dataframe."""

        X = self.variables.copy()
        data_features = list(X.columns)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
        pd.DataFrame(X_train, columns=data_features).to_csv(X_TRAIN, index=False)

        return X