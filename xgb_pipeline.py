from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
from preprocessor import preprocessor

# Pipeline completo:  preprocessamento + modelo XGBoost
xgb_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', XGBRegressor(random_state=42))
])