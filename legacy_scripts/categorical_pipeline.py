from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# Pipeline para transformação de features categóricas
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])
