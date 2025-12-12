import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv('spotify_songs.csv')

# Selecionar apenas colunas numéricas
df_numeric = df.select_dtypes(include=[np.number])

# Calcular a matriz de correlação
correlation_matrix = df_numeric.corr()

# Ordenar as colunas por correlação com 'popularity' (se existir)
if 'popularity' in correlation_matrix.columns:
    # Obter correlações com popularity em ordem decrescente (valor absoluto)
    popularity_corr = correlation_matrix['popularity'].abs().sort_values(ascending=False)
    sorted_columns = popularity_corr.index.tolist()
    
    # Reordenar a matriz de correlação
    correlation_matrix = correlation_matrix.loc[sorted_columns, sorted_columns]

# Criar o heatmap
plt.figure(figsize=(14, 12))
sns.heatmap(correlation_matrix, 
            annot=True,  # Exibir valores de correlação
            fmt='.2f',  # Formato com 2 casas decimais
            cmap='coolwarm',  # Cores que destacam correlações fortes (azul=negativa, vermelho=positiva)
            center=0,  # Centralizar a escala de cores no zero
            square=True,  # Células quadradas
            linewidths=0.5,  # Linhas entre células
            cbar_kws={'shrink': 0.8, 'label': 'Coeficiente de Correlação'},  # Barra de cores
            vmin=-1, vmax=1)  # Escala de -1 a 1

# Adicionar título
plt.title('Matriz de Correlação - Foco na Popularidade das Músicas no Spotify', 
          fontsize=16, fontweight='bold', pad=20)

# Rotacionar labels para melhor visualização
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Ajustar layout
plt.tight_layout()

# Salvar a figura
plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')

# Exibir o gráfico
plt.show()

print("Heatmap salvo como 'correlation_heatmap.png'")

# Exibir as correlações com 'popularity' em ordem decrescente
if 'popularity' in df_numeric.columns:
    print("\n" + "="*80)
    print("CORRELAÇÕES COM A POPULARIDADE (ordenadas por valor absoluto)")
    print("="*80 + "\n")
    
    popularity_correlations = correlation_matrix['popularity'].sort_values(ascending=False)
    
    for feature, corr_value in popularity_correlations.items():
        if feature != 'popularity':
            correlation_strength = ''
            if abs(corr_value) >= 0.7:
                correlation_strength = '🔴 FORTE'
            elif abs(corr_value) >= 0.4:
                correlation_strength = '🟡 MODERADA'
            elif abs(corr_value) >= 0.2:
                correlation_strength = '🟢 FRACA'
            else:
                correlation_strength = '⚪ MUITO FRACA'
            
            print(f"{feature:30s}: {corr_value:+.3f}  {correlation_strength}")
    
    print("\n" + "="*80 + "\n")
