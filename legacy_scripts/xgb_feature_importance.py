"""
Script para extrair a importância das features do modelo XGBoost
"""

import pandas as pd
import numpy as np

# Assumindo que xgb_pipeline já foi treinado e feature_names está disponível
# from xgb_pipeline import xgb_pipeline
# from get_feature_names import feature_names

# Extrair o modelo XGBoost treinado do pipeline
xgb_model = xgb_pipeline.named_steps['regressor']

# Obter a importância das features
feature_importances = xgb_model.feature_importances_

# Criar DataFrame com nome da feature e sua importância
importance_df = pd.DataFrame({
    'feature': feature_names,
    'importance': feature_importances
})

# Ordenar por importância (decrescente)
importance_df = importance_df.sort_values('importance', ascending=False).reset_index(drop=True)

# Exibir informações
print("="*80)
print("IMPORTÂNCIA DAS FEATURES - MODELO XGBoost")
print("="*80)
print(f"\nTotal de features: {len(importance_df)}")
print(f"Soma das importâncias: {importance_df['importance'].sum():.4f}")

print("\n" + "-"*80)
print("TOP 20 FEATURES MAIS IMPORTANTES")
print("-"*80)
print(f"{'#': <5} {'Feature':<40} {'Importância':<15} {'% Acumulado':<15}")
print("-"*80)

cumulative_importance = 0
for idx, row in importance_df.head(20).iterrows():
    cumulative_importance += row['importance']
    print(f"{idx+1:<5} {row['feature']:<40} {row['importance']:<15.6f} {cumulative_importance*100:<15.2f}%")

print("\n" + "="*80)

# Estatísticas
print("\nESTATÍSTICAS DAS IMPORTÂNCIAS:")
print("-"*80)
print(f"Média:           {importance_df['importance'].mean():.6f}")
print(f"Mediana:        {importance_df['importance'].median():.6f}")
print(f"Desvio padrão:  {importance_df['importance'].std():.6f}")
print(f"Mínimo:         {importance_df['importance'].min():.6f}")
print(f"Máximo:         {importance_df['importance'].max():.6f}")

# Análise de concentração
top_5_importance = importance_df.head(5)['importance'].sum()
top_10_importance = importance_df.head(10)['importance'].sum()
top_20_importance = importance_df.head(20)['importance'].sum()

print("\n" + "-"*80)
print("ANÁLISE DE CONCENTRAÇÃO:")
print("-"*80)
print(f"Top 5 features:   {top_5_importance*100:.2f}% da importância total")
print(f"Top 10 features: {top_10_importance*100:.2f}% da importância total")
print(f"Top 20 features: {top_20_importance*100:.2f}% da importância total")

# Salvar o DataFrame
importance_df.to_csv('xgb_feature_importance.csv', index=False)
print("\n✅ DataFrame salvo como 'xgb_feature_importance.csv'")

print("\n" + "="*80)
print("✅ DataFrame 'importance_df' criado com sucesso!")
print("   Colunas: ['feature', 'importance']")
print(f"   Shape: {importance_df.shape}")
