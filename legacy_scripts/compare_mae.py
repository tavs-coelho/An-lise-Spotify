import matplotlib.pyplot as plt

# Dados para o gráfico
models = ['Ridge Regression', 'XGBoost']
mae_values = [mae_ridge, mae_xgb]

# Criar gráfico de barras
plt.figure(figsize=(10, 6))
bars = plt.bar(models, mae_values, color=['#1f77b4', '#ff7f0e'], alpha=0.8)

# Adicionar valores nas barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.4f}',
             ha='center', va='bottom', fontsize=12, fontweight='bold')

# Configurações do gráfico
plt.ylabel('MAE (Mean Absolute Error)', fontsize=12, fontweight='bold')
plt.xlabel('Modelo', fontsize=12, fontweight='bold')
plt.title('Comparação de MAE: Ridge vs XGBoost', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()

# Salvar e mostrar
plt.savefig('mae_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("Gráfico salvo como 'mae_comparison.png')")
