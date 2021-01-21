from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from support_vector_machine.config import config
from support_vector_machine.preprocessing import preprocessors as pp
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

SVR_model = SVR()
# pipe = Pipeline(steps=[('svr', SVR_model)])
