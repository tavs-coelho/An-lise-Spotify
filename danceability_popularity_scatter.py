import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv('spotify_songs.csv')

# Criar o scatter plot com linha de regressão
plt.figure(figsize=(12, 7))

# Usar regplot do seaborn para scatter plot com linha de regressão
sns.regplot(data=df, 
            x='danceability', 
            y='popularity',
            scatter_kws={'alpha': 0.3, 'color': 'steelblue', 's': 30},  # Configurações dos pontos
            line_kws={'color': 'red', 'linewidth': 2.5, 'label': 'Linha de Regressão'})  # Configurações da linha

# Adicionar título e labels
plt.title('Relação entre Danceability e Popularity no Spotify', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Danceability (Dançabilidade)', fontsize=13, fontweight='bold')
plt.ylabel('Popularity (Popularidade)', fontsize=13, fontweight='bold')

# Adicionar grid para melhor visualização
plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.7)

# Adicionar legenda
plt.legend(fontsize=11)

# Ajustar layout
plt.tight_layout()

# Salvar a figura
plt.savefig('danceability_popularity_scatter.png', dpi=300, bbox_inches='tight')

# Exibir o gráfico
plt.show()

print("Gráfico salvo como 'danceability_popularity_scatter.png'")

# Calcular e exibir estatísticas da correlação
if 'danceability' in df.columns and 'popularity' in df.columns:
    # Remover valores nulos para cálculo preciso
    df_clean = df[['danceability', 'popularity']].dropna()
    
    # Calcular correlação de Pearson
    correlation = df_clean['danceability'].corr(df_clean['popularity'])
    
    # Calcular R² (coeficiente de determinação)
    r_squared = correlation ** 2
    
    print("\n" + "="*80)
    print("ANÁLISE DA RELAÇÃO: DANCEABILITY vs POPULARITY")
    print("="*80 + "\n")
    
    print(f"Coeficiente de Correlação (Pearson): {correlation:+.4f}")
    print(f"Coeficiente de Determinação (R²): {r_squared:.4f}")
    print(f"Percentual de variância explicada: {r_squared * 100:.2f}%")
    
    print("\n" + "-"*80)
    print("INTERPRETAÇÃO:")
    print("-"*80 + "\n")
    
    # Interpretar a correlação
    if abs(correlation) >= 0.7:
        strength = "FORTE"
    elif abs(correlation) >= 0.4:
        strength = "MODERADA"
    elif abs(correlation) >= 0.2:
        strength = "FRACA"
    else:
        strength = "MUITO FRACA"
    
    direction = "POSITIVA" if correlation > 0 else "NEGATIVA"
    
    print(f"✓ Correlação {strength} e {direction}")
    
    if correlation > 0:
        print(f"✓ Músicas com maior dançabilidade tendem a ter maior popularidade.")
    else:
        print(f"✓ Músicas com maior dançabilidade tendem a ter menor popularidade.")
    
    print(f"✓ A dançabilidade explica aproximadamente {r_squared * 100:.2f}% da variação na popularidade.")
    
    if r_squared < 0.1:
        print(f"⚠ A dançabilidade sozinha NÃO é um bom preditor de popularidade.")
    elif r_squared < 0.3:
        print(f"⚠ A dançabilidade tem influência limitada na popularidade.")
    else:
        print(f"✓ A dançabilidade é um fator relevante para a popularidade.")
    
    print("\n" + "="*80 + "\n")
