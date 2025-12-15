"""
Feature Configuration Module

Defines the features used in the machine learning models.
This configuration is used by the legacy scripts.

For production use, see config.yaml for centralized configuration.

Author: Geyson de Araujo
Date: December 2025
"""

# Lista de features numéricas para StandardScaler
NUM_FEATURES = [
    'danceability',
    'energy',
    'loudness',
    'speechiness',
    'acousticness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo',
    'duration_ms'
]

# Lista de features categóricas para OneHotEncoder
CAT_FEATURES = [
    'key',
    'mode',
    'time_signature'
]

