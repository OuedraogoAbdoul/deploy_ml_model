from support_vector_machine.config import config
from support_vector_machine.preprocessing.data_manager import load_dataset, save_model
from support_vector_machine import model_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
import pandas as pd

def train_svm_model():
    full_train_data = load_dataset(config.TRAININGDATA)
    y = full_train_data[config.TARGET]
    X = full_train_data.loc[:, full_train_data.columns != config.TARGET]
    X = pd.get_dummies(X)

    scaler = MinMaxScaler()
    X = pd.DataFrame(scaler.fit_transform(X))

    # split the DATASETDIR
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=config.SEED)
    # X_train.to_csv(f"{config.DATASETDIR}/X_train.csv", index=False)
    # X_test.to_csv(f"{config.DATASETDIR}/X_test.csv", index=False)
    # y_train.to_csv(f"{config.DATASETDIR}/y_train.csv", index=False)
    # y_test.to_csv(f"{config.DATASETDIR}/y_test.csv", index=False)
    parameters = [{'C': [1, 10, 100, 1000], 'kernel': ['linear']},
        {'C': [1, 10, 100, 1000], 'kernel': ['rbf'], 'gamma': [0.5, 0.1, 0.01, 0.001, 0.0001]}]
    clf = GridSearchCV(model_pipeline.SVR_model, parameters)

    clf.fit(X_train, y_train)
    save_model(save_model=clf.best_estimator_)


if __name__ == '__main__':
    train_svm_model()
