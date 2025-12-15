# Separar features (X) e target (y)
X = df.drop('popularity', axis=1)
y = df['popularity']