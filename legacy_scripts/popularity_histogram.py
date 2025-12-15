import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv('spotify_songs.csv')

# Criar o histograma com KDE da coluna 'popularity'
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='popularity', kde=True, bins=30, color='skyblue', edgecolor='black')

# Adicionar título e labels
plt.title('Distribuição da Popularidade das Músicas no Spotify', fontsize=16, fontweight='bold')
plt.xlabel('Popularidade', fontsize=12)
plt.ylabel('Frequência', fontsize=12)

# Ajustar layout
plt.tight_layout()

# Salvar a figura
plt.savefig('popularity_histogram.png', dpi=300, bbox_inches='tight')

# Exibir o gráfico
plt.show()

print("Gráfico salvo como 'popularity_histogram.png'")

# Análise de assimetria
print("\n" + "="*80)
print("ANÁLISE DE ASSIMETRIA DA POPULARIDADE")
print("="*80 + "\n")

# Calcular métricas de assimetria
skewness = df['popularity'].skew()
mean_pop = df['popularity'].mean()
median_pop = df['popularity'].median()

print(f"Coeficiente de Assimetria (Skewness): {skewness:.3f}")
print(f"Média: {mean_pop:.2f}")
print(f"Mediana: {median_pop:.2f}")

print("\n" + "-"*80)
print("CONCLUSÃO:")
print("-"*80 + "\n")

# Conclusão baseada na assimetria
if abs(skewness) < 0.5:
    print("✓ A distribuição da popularidade é aproximadamente SIMÉTRICA (skewness < 0.5).")
    print("✓ Transformação logarítmica NÃO é necessária.")
    print("✓ Os dados podem ser utilizados diretamente em modelos que assumem normalidade.")
elif skewness > 0.5:
    print("⚠ A distribuição da popularidade apresenta ASSIMETRIA POSITIVA (skewness > 0.5).")
    print("⚠ Há uma concentração de músicas com baixa popularidade e uma cauda longa à direita.")
    print("⚠ Transformação logarítmica PODE SER NECESSÁRIA para:")
    print("   - Reduzir o impacto de outliers")
    print("   - Melhorar a performance de modelos lineares")
    print("   - Aproximar a distribuição de uma normal")
    print("\n   Recomendação: Aplicar log(popularity + 1) para evitar problemas com zeros.")
else:
    print("⚠ A distribuição da popularidade apresenta ASSIMETRIA NEGATIVA (skewness < -0.5).")
    print("⚠ Há uma concentração de músicas com alta popularidade e uma cauda longa à esquerda.")
    print("⚠ Transformação logarítmica pode NÃO ser apropriada.")
    print("   Recomendação: Considerar outras transformações (ex: Box-Cox, Yeo-Johnson).")

print("\n" + "="*80 + "\n")
