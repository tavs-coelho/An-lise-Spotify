# Histórico de Mudanças

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/spec/v2.0.0.html).

## [1.0.0] - 2025-12-15

### Adicionado
- Estrutura de pacote profissional completa com `src/spotify_analysis/`
- API REST FastAPI para servir modelos com documentação OpenAPI
- Dashboard interativo Streamlit com interface de predição em tempo real
- Suporte Docker e Docker Compose para implantação containerizada
- Pipeline CI/CD abrangente com GitHub Actions
- Testes unitários e de integração com pytest
- Integração de ferramentas de qualidade de código (black, flake8, mypy, isort, bandit)
- Type hints em todas as funções
- Docstrings abrangentes seguindo estilo Google
- Módulo de processamento de dados com pipelines de pré-processamento
- Módulo de treinamento de modelos com 6 algoritmos de regressão
- Utilitários de visualização com plots de qualidade de publicação
- Sistema de gerenciamento de configuração
- Utilitários de logging e tratamento de erros
- Licença MIT para distribuição open source
- README profissional com badges e documentação
- CONTRIBUTING.md com diretrizes de desenvolvimento
- Makefile para tarefas comuns de desenvolvimento
- Requirements.txt com dependências fixadas
- pyproject.toml para empacotamento Python moderno

### Modificado
- Reorganizada estrutura do projeto seguindo melhores práticas Python
- Movidos scripts legados para pasta `legacy_scripts/`
- Movida documentação para pasta `docs/`
- Movido notebook para pasta `notebooks/`
- Atualizado README com instruções abrangentes

### Corrigido
- Erros de importação e dependências de módulos
- Problemas de segurança identificados pelo CodeQL
- Problemas de qualidade de código identificados por linters
- Dependências duplicadas em requirements.txt
- Permissões ausentes no workflow do GitHub Actions

### Segurança
- Adicionado scan de segurança com bandit
- Implementadas permissões apropriadas de GITHUB_TOKEN
- Adicionadas verificações de segurança de dependências com safety

## [0.1.0] - Lançamento Inicial

### Adicionado
- Notebook básico de análise
- Scripts Python simples para processamento de dados
- Treinamento de modelo XGBoost
- Visualizações básicas
- Relatório técnico em português
