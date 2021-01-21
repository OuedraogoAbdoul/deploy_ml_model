from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from support_vector_machine.config import config
from support_vector_machine.preprocessing import preprocessors as pp
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV


SVR_model =  SVR()
# pipe  = Pipeline(steps=[('svr', SVR_model)])
parameters = [{'C': [1, 10, 100, 1000], 'kernel': ['linear']},{'C': [1, 10, 100, 1000], 'kernel': ['rbf'], 'gamma': [0.5, 0.1, 0.01, 0.001, 0.0001]}]
clf = GridSearchCV(SVR_model, parameters, scoring="neg_mean_squared_error", cv=5, verbose=3)
# pipe = Pipeline(steps=[('svr', SVR_model)])
