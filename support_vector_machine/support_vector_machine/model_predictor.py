from support_vector_machine.config import config
from support_vector_machine import model_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error

from support_vector_machine.preprocessing.data_manager import load_dataset, save_model, load_model
from support_vector_machine.preprocessing.prediction_input_validator import validate_input_data


def make_prediction():

    X_test,y_true  = validate_input_data(config.TESTDATA)

    svr_predict = load_model()
    y_pred = svr_predict.predict(X_test)
    mean_absolute_error_ = mean_absolute_error(y_true, y_pred)
    mean_squared_error_ = mean_absolute_error(y_true, y_pred)
    
    print(f"Model mean_absolute_error: {mean_absolute_error_}")
    print(f"Model mean_squared_error: {mean_squared_error_}")


if __name__ == '__main__':
    make_prediction()
