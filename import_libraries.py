"""
Data Exploration Script - Initial Data Loading and Statistics

This script demonstrates basic data loading and exploration using pandas.
For production use, see the structured implementation in src/data/loader.py

Author: Geyson de Araujo
Date: December 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv('spotify_songs.csv')

# Exibir as 5 primeiras linhas do DataFrame
print("5 primeiras linhas do DataFrame:")
print(df.head())
print("\n" + "="*80 + "\n")

# Exibir informações sobre o DataFrame (tipos de dados e valores não nulos)
print("Informações sobre o DataFrame:")
print(df.info())
print("\n" + "="*80 + "\n")

# Exibir estatísticas descritivas das colunas numéricas
print("Estatísticas descritivas das colunas numéricas:")
print(df.describe())
print("\n" + "="*80 + "\n")

# Calcular e exibir a soma de valores ausentes por coluna em ordem decrescente
print("Valores ausentes por coluna (ordem decrescente):")
valores_ausentes = df.isnull().sum().sort_values(ascending=False)
print(valores_ausentes)
