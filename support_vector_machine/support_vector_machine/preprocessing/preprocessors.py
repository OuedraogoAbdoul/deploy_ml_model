from sklearn.base import BaseEstimator, TransformerMixin

class CategoricalInputHandler(BaseEstimator, TransformerMixin):
    """docstring for ."""

    def __init__(self, arg):
        self.arg = arg


class NumericalInputHandler(BaseEstimator, TransformerMixin):
    """docstring for ."""

    def __init__(self, arg):
        self.arg = arg
