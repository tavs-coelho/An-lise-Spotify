# Diretório de Assets

Este diretório contém assets visuais para a documentação do projeto.

## 📁 Estrutura de Diretórios

```
assets/
├── screenshots/          # Screenshots em alta resolução da aplicação
│   ├── dashboard_preview.png      # Interface do dashboard Streamlit
│   ├── api_preview.png            # Documentação FastAPI
│   ├── architecture.png           # Diagrama de arquitetura do sistema
│   ├── results_summary.png        # Desempenho do modelo e insights
│   └── feature_analysis.png       # Importância de features e correlações
│
├── demo/                 # Recursos de vídeo demo e guias
│   └── DEMO_GUIDE.md             # Instruções para criar vídeos demo
│
└── generate_screenshots.py        # Script para regenerar screenshots

```

## 🎨 Screenshots

Todos os screenshots são gerados programaticamente usando matplotlib e seaborn para garantir consistência e reprodutibilidade.

### Geração

Para regenerar todos os screenshots:

```bash
python assets/generate_screenshots.py
```

Requisitos:
- matplotlib
- seaborn
- pandas
- numpy

### Especificações

- **Formato:** PNG
- **Resolução:** 150 DPI
- **Cor:** Cor completa com fundo branco
- **Tamanho:** Otimizado para web e impressão

## 📸 Descrições de Screenshots

### 1. dashboard_preview.png
**Dimensões:** ~1600x1200px  
**Conteúdo:** 
- Visão geral de métricas do projeto
- Gráfico de importância de features
- Barras de comparação de modelos
- Histograma de distribuição de popularidade

### 2. api_preview.png
**Dimensões:** ~1400x1000px  
**Conteúdo:**
- Lista de endpoints FastAPI com métodos HTTP
- Formato de exemplo de requisição/resposta
- Link de documentação interativa

### 3. architecture.png
**Dimensões:** ~1400x1000px  
**Conteúdo:**
- Camadas de arquitetura do sistema
- Interações de componentes
- Visualização de fluxo de dados

### 4. results_summary.png
**Dimensões:** ~1400x1000px  
**Conteúdo:**
- Comparações de MAE e R² dos modelos
- Distribuição de importância de features
- Resumo de insights principais

### 5. feature_analysis.png
**Dimensões:** ~1400x1000px  
**Conteúdo:**
- Gráficos de dispersão de relacionamentos de features
- Mapa de calor de correlação
- Comparações de distribuição

## 🎥 Recursos de Demo

Veja `demo/DEMO_GUIDE.md` para instruções abrangentes sobre:
- Criar vídeos demo
- Gravar capturas de tela
- Fazer GIFs animados
- Publicar demos

## 📝 Diretrizes de Uso

### Na Documentação
```markdown
![Prévia do Dashboard](assets/screenshots/dashboard_preview.png)
```

### Em Apresentações
- Todas as imagens são em alta resolução e adequadas para apresentações
- Use com atribuição adequada ao projeto

### Em Relatórios Acadêmicos
- Screenshots demonstram a implementação prática
- Podem ser incluídos nas seções de metodologia e resultados

## 🔄 Atualizando Assets

Ao atualizar o projeto:

1. **Mudanças Visuais:** Se a UI mudar, regenere os screenshots
2. **Novas Funcionalidades:** Adicione novos screenshots mostrando-as
3. **Consistência:** Mantenha estilo visual consistente em todos os assets
4. **Documentação:** Atualize este README com novas descrições de assets

## 📄 Licença

Todos os assets visuais neste diretório são parte do projeto de Análise do Spotify e estão licenciados sob a Licença MIT, consistente com a licença do projeto.

## 🙏 Créditos

Screenshots gerados usando:
- **matplotlib** - Biblioteca de plotagem
- **seaborn** - Visualização estatística
- **Python** - Automação e scripting

---

*Última atualização: Dezembro 2025*
