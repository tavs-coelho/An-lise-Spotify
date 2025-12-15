# 1. Entendimento do Negócio (Business Understanding)

## 📊 Contexto do Problema

A indústria do streaming musical movimenta bilhões de dólares anualmente, e plataformas como o Spotify hospedam milhões de músicas. Compreender quais características musicais influenciam a popularidade de uma faixa é fundamental para:

- **Artistas independentes**: otimizar a produção musical com base em dados
- **Gravadoras e produtores**: tomar decisões de investimento mais assertivas
- **Plataformas de streaming**: melhorar sistemas de curadoria e recomendação
- **Profissionais de marketing musical**: direcionar estratégias promocionais

## 🎯 Problema de Negócio

**Como prever a popularidade de músicas no Spotify com base em suas características musicais objetivas?**

A popularidade no Spotify é influenciada por diversos fatores: características musicais (ritmo, energia, valência), contexto de lançamento, artista, marketing, e tendências culturais. Este projeto foca em responder se as **features musicais intrínsecas** podem explicar e prever popularidade.

## 🔍 Perguntas de Negócio

1. **Quais características musicais têm maior influência na popularidade de uma música?**
2. **É possível prever com precisão a popularidade de uma música baseado apenas em suas features?**
3. **Existem perfis distintos de músicas populares? (clusters naturais)**
4. **Podemos classificar músicas em categorias de popularidade (alta/média/baixa)?**
5. **Como recomendar músicas similares com base em características musicais?**

## 🎯 Objetivos do Projeto

### Objetivo Geral
Desenvolver um sistema de predição de popularidade musical utilizando técnicas de Machine Learning, seguindo a metodologia CRISP-DM.

### Objetivos Específicos
1. Realizar análise exploratória completa do dataset Spotify Songs
2. Identificar as features mais relevantes para popularidade
3. Treinar e comparar múltiplos modelos de **regressão** para prever popularidade
4. Desenvolver um modelo de **classificação** para categorizar músicas
5. Aplicar **clustering** para descobrir perfis musicais naturais
6. Implementar um **sistema de recomendação** baseado em similaridade

## 📈 Métricas de Sucesso (KPIs)

### Para Regressão (Predição de Popularidade)
- **R² (Coeficiente de Determinação)**: Meta > 0.20
  - Indica quanto da variância na popularidade é explicada pelas features
- **MAE (Mean Absolute Error)**: Meta < 15 pontos
  - Erro médio absoluto aceitável na escala 0-100

### Para Classificação (Alta/Média/Baixa Popularidade)
- **Accuracy**: Meta > 0.60
- **F1-Score**: Meta > 0.55 (especialmente para classe "Alta")
- **Precision/Recall balanceados**: evitar viés em classes específicas

### Para Clustering
- **Silhouette Score**: Meta > 0.30
  - Qualidade da separação entre clusters
- **Interpretabilidade**: clusters devem ter perfis musicais distintos e interpretáveis

### Para Sistema de Recomendação
- **Precision@5**: Meta > 0.70
  - Das 5 músicas recomendadas, 70% devem ser relevantes/similares
- **Diversidade**: recomendações devem cobrir diferentes perfis musicais

## 💼 Impacto Esperado

### Para o Negócio
- **Artistas**: insights sobre quais características priorizar na produção
- **Gravadoras**: ferramentas de apoio à decisão para investimentos
- **Plataformas**: melhoria em sistemas de curadoria automática

### Para o Conhecimento
- Compreensão quantitativa dos fatores que influenciam popularidade musical
- Limitações da predição baseada apenas em features intrínsecas
- Identificação de características que transcendem gêneros musicais

## ⚠️ Limitações Conhecidas

1. **Popularidade é multifatorial**: features musicais são apenas parte da explicação
   - Marketing, momento de lançamento, e viralidade não estão nos dados
2. **Dados históricos**: popularidade muda ao longo do tempo
3. **Viés de plataforma**: dados do Spotify podem não representar todas as audiências
4. **Causalidade vs Correlação**: identificar relações não implica causalidade

## 🎓 Justificativa Acadêmica

Este projeto aplica o **ciclo completo de CRISP-DM** em um problema real, demonstrando competências em:

- ✅ Formulação de problemas de negócio
- ✅ Análise exploratória de dados (EDA)
- ✅ Engenharia de features e preparação de dados
- ✅ **Aprendizado Supervisionado** (Regressão e Classificação)
- ✅ **Aprendizado Não Supervisionado** (Clustering)
- ✅ **Sistemas de Recomendação**
- ✅ Avaliação crítica de modelos
- ✅ Comunicação de resultados

---

**Próximas Etapas**: Análise Exploratória de Dados (EDA) e preparação para modelagem.