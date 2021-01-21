from sklearn.base import BaseEstimator, TransformerMixin

class FillnaCategoricalImputs(BaseEstimator, TransformerMixin):
    """docstring for ."""

    def __init__(self, cat_columns):
        self.cat_columns = cat_columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        X = X.copy()
        for feature in self.cat_columns:
            X[feature] = x[feature].fillna("missing")

        return X


class FillnaNumericalImputs(BaseEstimator, TransformerMixin):
    """docstring for ."""

    def __init__(self, num_columns):
        self.num_columns = num_columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        X = X.copy()
        for feature in self.num_columns:
            X[feature] = x[feature].fillna("missing")

        return X

class DropFeatures(BaseEstimator, TransformerMixin):
    """docstring for ."""

    def __init__(self, unused_columns):
        self.unused_columns = unused_columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        X = X.copy()
        X = X.drop(self.unused_columns, axis=1)
        return X
