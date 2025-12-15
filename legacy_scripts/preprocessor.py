from sklearn.compose import ColumnTransformer
from features_config import NUM_FEATURES, CAT_FEATURES
from numeric_pipeline import numeric_transformer
from categorical_pipeline import categorical_transformer

# ColumnTransformer que aplica transformações específicas para cada tipo de feature
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, NUM_FEATURES),
        ('cat', categorical_transformer, CAT_FEATURES)
    ])
