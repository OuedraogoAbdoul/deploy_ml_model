from regression_model import pipeline as pipeline

def train_models():
    
    pipeline.btc_price_pipeline.fit(X_train[config.FEATURES], y_train)