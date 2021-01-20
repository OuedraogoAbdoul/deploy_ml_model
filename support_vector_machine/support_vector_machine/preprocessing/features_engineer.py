from sklearn.base import BaseEstimator, TransformerMixin

class FeatureTransformation(BaseEstimator, TransformerMixin):
    """docstring for ."""

    def __init__(self, arg):
        self.arg = arg

class FeatureSelection(BaseEstimator, TransformerMixin):
    """docstring for ."""

    def __init__(self, arg):
        self.arg = arg
