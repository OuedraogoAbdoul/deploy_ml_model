from support_vector_machine.config import config
from support_vector_machine.preprocessing.data_manager import load_dataset
from support_vector_machine import model_pipeline
from sklearn.model_selection import train_test_split


def train_svm_model():
    full_train_data = load_dataset(config.TRAININGDATA)
    y = full_train_data[config.TARGET]
    X = full_train_data.drop([config.DROPFEATURES, config.TARGET])


    # split the DATASETDIR
    X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=config.SEED)

    print(model_pipeline.svm_pipeline.fit(X_train.values, y_train.values))


if __name__ == '__main__':
    train_svm_model()
