# Treinar o pipeline XGBoost
xgb_pipeline.fit(X_train, y_train)

# Gerar previsões no conjunto de teste
y_pred_xgb = xgb_pipeline.predict(X_test)