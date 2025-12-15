# Diretório de Dados

Este diretório contém os datasets usados no projeto de Análise de Popularidade de Músicas no Spotify.

## Dataset

### Dataset Spotify Songs

O principal dataset usado neste projeto é o dataset **Spotify Songs**, que contém características de áudio para milhares de faixas.

#### Instruções de Download

Devido a limitações de tamanho, o dataset não está incluído neste repositório. Por favor, baixe-o usando um dos seguintes métodos:

##### Opção 1: API do Kaggle (Recomendado)

```bash
# Instale a API do Kaggle
pip install kaggle

# Configure credenciais do Kaggle (coloque kaggle.json em ~/.kaggle/)
# Baixe o dataset
kaggle datasets download -d zaheenhamidani/ultimate-spotify-tracks-db

# Descompacte no diretório data
unzip ultimate-spotify-tracks-db.zip -d data/
```

##### Opção 2: Download Manual

1. Visite [Kaggle - Ultimate Spotify Tracks DB](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)
2. Baixe o arquivo CSV
3. Coloque-o neste diretório como `spotify_songs.csv`

#### Informações do Dataset

- **Linhas:** ~113.999 faixas
- **Colunas:** 23 características
- **Tamanho:** ~15 MB
- **Formato:** CSV

## Dados de Exemplo

Para fins de teste, a aplicação pode gerar dados de exemplo se o dataset principal não estiver disponível.
