# Contribuindo para Análise de Popularidade de Músicas no Spotify

Primeiramente, obrigado por considerar contribuir para este projeto! 🎉

## Índice

- [Código de Conduta](#código-de-conduta)
- [Como Posso Contribuir?](#como-posso-contribuir)
- [Configuração de Desenvolvimento](#configuração-de-desenvolvimento)
- [Padrões de Codificação](#padrões-de-codificação)
- [Diretrizes de Commit](#diretrizes-de-commit)
- [Processo de Pull Request](#processo-de-pull-request)

## Código de Conduta

Este projeto adere a um Código de Conduta. Ao participar, espera-se que você mantenha este código. Por favor, reporte comportamento inaceitável aos mantenedores do projeto.

### Nossos Padrões

- **Seja respeitoso** e inclusivo
- **Seja colaborativo** e construtivo
- **Foque no que é melhor** para a comunidade
- **Mostre empatia** com outros membros da comunidade

## Como Posso Contribuir?

### Reportando Bugs

Antes de criar relatórios de bugs, por favor verifique os issues existentes. Ao criar um relatório de bug, inclua:

- **Título e descrição claros**
- **Passos para reproduzir** o problema
- **Comportamento esperado vs. comportamento real**
- **Informações do sistema** (SO, versão do Python, etc.)
- **Amostras de código** se aplicável

### Sugerindo Melhorias

Sugestões de melhorias são rastreadas como GitHub issues. Ao criar uma sugestão de melhoria, inclua:

- **Título e descrição claros**
- **Justificativa** para a melhoria
- **Abordagem de implementação** possível
- **Exemplos** de como funcionaria

### Pull Requests

- Preencha o template requerido
- Siga os padrões de codificação
- Inclua testes para novas funcionalidades
- Atualize a documentação conforme necessário
- Certifique-se de que o pipeline CI/CD passe

## Configuração de Desenvolvimento

### 1. Fork e Clone

```bash
# Faça fork do repositório no GitHub
# Clone seu fork
git clone https://github.com/SEU_USUARIO/An-lise-Spotify.git
cd An-lise-Spotify

# Adicione remote upstream
git remote add upstream https://github.com/tavs-coelho/An-lise-Spotify.git
```

### 2. Crie Ambiente de Desenvolvimento

```bash
# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale dependências
pip install -r requirements.txt
pip install -e .

# Instale dependências de desenvolvimento
pip install pytest pytest-cov black flake8 mypy isort bandit
```

### 3. Crie Branch de Feature

```bash
git checkout -b feature/nome-da-sua-feature
```

## Padrões de Codificação

### Guia de Estilo Python

Este projeto segue **PEP 8** com algumas modificações:

- **Comprimento de linha:** 100 caracteres (não 79)
- **Aspas de string:** Use aspas duplas para strings
- **Imports:** Organizados com isort
- **Formatação:** Black para auto-formatação

### Type Hints

Todas as funções devem incluir type hints:

```python
def process_data(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Processa o DataFrame.
    
    Args:
        df: DataFrame de entrada
        threshold: Limiar de processamento
        
    Returns:
        DataFrame processado
    """
    # Implementação
    return df
```

### Documentação

Todos os módulos, classes e funções devem ter docstrings:

```python
def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """Calcula métricas de avaliação.
    
    Computa MAE, MSE, RMSE e pontuação R² para as predições.
    
    Args:
        y_true: Valores verdadeiros
        y_pred: Valores preditos
        
    Returns:
        Dicionário contendo nomes e valores das métricas
        
    Raises:
        ValueError: Se os arrays tiverem formas diferentes
        
    Example:
        >>> y_true = np.array([1, 2, 3])
        >>> y_pred = np.array([1.1, 2.1, 2.9])
        >>> metrics = calculate_metrics(y_true, y_pred)
        >>> print(metrics['mae'])
        0.1
    """
    # Implementação
```

### Testes

- Escreva testes unitários para todas as novas funcionalidades
- Busque >80% de cobertura de código
- Use nomes de teste descritivos
- Siga o padrão AAA (Arrange, Act, Assert)

```python
def test_model_training_with_valid_data():
    """Testa que o modelo treina com sucesso com dados de entrada válidos."""
    # Arrange (Preparar)
    X_train = np.random.randn(100, 10)
    y_train = np.random.randint(0, 100, 100)
    trainer = ModelTrainer('xgboost')
    
    # Act (Agir)
    trainer.fit(X_train, y_train)
    
    # Assert (Verificar)
    assert trainer.is_fitted
    assert trainer.model is not None
```

## Ferramentas de Qualidade de Código

### Execute Antes de Commitar

```bash
# Formate o código
black src/ tests/

# Ordene imports
isort src/ tests/

# Verifique qualidade do código
flake8 src/ tests/

# Verificação de tipos
mypy src/

# Execute testes
pytest

# Scan de segurança
bandit -r src/
```

### Hook de Pre-commit (Opcional)

Crie `.git/hooks/pre-commit`:

```bash
#!/bin/bash
black src/ tests/ --check
isort src/ tests/ --check-only
flake8 src/ tests/
pytest
```

## Diretrizes de Commit

### Formato de Mensagem de Commit

```
<tipo>(<escopo>): <assunto>

<corpo>

<rodapé>
```

### Tipos

- **feat:** Nova funcionalidade
- **fix:** Correção de bug
- **docs:** Mudanças na documentação
- **style:** Mudanças de estilo de código (formatação, etc.)
- **refactor:** Refatoração de código
- **test:** Adição ou atualização de testes
- **chore:** Tarefas de manutenção

### Exemplos

```
feat(models): adiciona explicador SHAP para interpretabilidade de modelo

Implementou cálculo de valores SHAP para fornecer explicações
detalhadas para predições do XGBoost.

Closes #123
```

```
fix(api): corrige erro de validação no endpoint de predição

Corrigido problema onde certos valores de entrada válidos estavam sendo
rejeitados devido a limites de validação incorretos.

Fixes #456
```

## Processo de Pull Request

### Antes de Enviar

1. **Atualize seu fork:**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Execute todas as verificações:**
   ```bash
   make test  # Ou execute testes manualmente
   black src/ tests/
   flake8 src/ tests/
   ```

3. **Atualize a documentação** se necessário

4. **Adicione testes** para novas funcionalidades

### Template de PR

Ao criar um PR, inclua:

- **Descrição:** O que este PR faz?
- **Motivação:** Por que essa mudança é necessária?
- **Teste:** Como foi testado?
- **Screenshots:** Se aplicável
- **Checklist:** 
  - [ ] Testes passam
  - [ ] Código formatado
  - [ ] Documentação atualizada
  - [ ] CHANGELOG atualizado (se aplicável)

### Processo de Revisão

- Mantenedores revisarão seu PR
- Responda aos comentários da revisão
- Mantenha o PR focado e pequeno
- Seja paciente e respeitoso

## Fluxo de Trabalho de Desenvolvimento

```bash
# 1. Sincronize com upstream
git checkout main
git fetch upstream
git merge upstream/main

# 2. Crie branch de feature
git checkout -b feature/minha-feature

# 3. Faça mudanças
# ... código, teste, commit ...

# 4. Execute verificações de qualidade
black src/ tests/
pytest
flake8 src/

# 5. Push para seu fork
git push origin feature/minha-feature

# 6. Crie Pull Request no GitHub
```

## Dúvidas?

Sinta-se livre para:
- Abrir um issue para perguntas
- Entrar em contato com mantenedores
- Participar de discussões

## Reconhecimento

Contribuidores serão reconhecidos em:
- Agradecimentos no README
- Arquivo CONTRIBUTORS.md
- Notas de lançamento

Obrigado por contribuir! 🎵✨
