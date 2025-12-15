# Guia de Contribuição

Obrigado por considerar contribuir para este projeto! Este documento fornece diretrizes para contribuir com o projeto de Análise de Popularidade no Spotify.

## 📋 Como Contribuir

### 1. Fork e Clone

```bash
# Fork o repositório no GitHub e depois:
git clone https://github.com/seu-usuario/An-lise-Spotify.git
cd An-lise-Spotify
```

### 2. Configure o Ambiente

```bash
# Crie um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 3. Crie uma Branch

```bash
# Crie uma branch para sua feature/correção
git checkout -b feature/nome-da-feature
# ou
git checkout -b fix/nome-do-bug
```

### 4. Faça suas Alterações

- Siga as convenções de código Python (PEP 8)
- Adicione docstrings para funções e classes
- Adicione testes quando apropriado
- Mantenha o código limpo e bem documentado

### 5. Teste suas Alterações

```bash
# Execute os testes
pytest tests/

# Verifique a cobertura
pytest --cov=src tests/

# Execute linting
flake8 src/
black --check src/
```

### 6. Commit e Push

```bash
# Adicione suas mudanças
git add .

# Faça commit com mensagem descritiva
git commit -m "feat: adiciona nova funcionalidade X"

# Push para seu fork
git push origin feature/nome-da-feature
```

### 7. Abra um Pull Request

- Vá para o repositório original no GitHub
- Clique em "New Pull Request"
- Selecione sua branch
- Descreva suas alterações detalhadamente

## 🎯 Convenções de Código

### Mensagens de Commit

Use o padrão Conventional Commits:

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Alterações na documentação
- `style:` Formatação, ponto-e-vírgula faltando, etc
- `refactor:` Refatoração de código
- `test:` Adição ou correção de testes
- `chore:` Tarefas de manutenção

Exemplos:
```
feat: adiciona modelo Random Forest
fix: corrige cálculo de MAE
docs: atualiza README com instruções de instalação
```

### Estilo de Código Python

- Siga PEP 8
- Use nomes descritivos para variáveis e funções
- Limite linhas a 88 caracteres (Black formatter)
- Adicione docstrings estilo Google

Exemplo:
```python
def calcular_popularidade(features: np.ndarray) -> float:
    """
    Calcula a popularidade prevista baseada nas features musicais.
    
    Args:
        features: Array numpy com features normalizadas
        
    Returns:
        Popularidade prevista (0-100)
        
    Raises:
        ValueError: Se features estiver vazio
    """
    if len(features) == 0:
        raise ValueError("Features não podem estar vazias")
    return model.predict(features)[0]
```

### Testes

- Escreva testes para novas funcionalidades
- Mantenha cobertura de testes > 80%
- Use pytest para testes
- Nomeie testes claramente: `test_nome_da_funcao_cenario`

Exemplo:
```python
def test_calcular_popularidade_valores_validos():
    features = np.array([0.5, 0.7, 0.3])
    resultado = calcular_popularidade(features)
    assert 0 <= resultado <= 100
```

## 📝 Relatando Bugs

Ao reportar um bug, inclua:

1. **Descrição clara** do problema
2. **Passos para reproduzir** o bug
3. **Comportamento esperado** vs **comportamento atual**
4. **Ambiente**: SO, versão do Python, versões de bibliotecas
5. **Screenshots** se aplicável

## 💡 Sugerindo Melhorias

Para sugerir melhorias:

1. Verifique se já não existe uma issue similar
2. Descreva claramente a melhoria proposta
3. Explique o benefício da melhoria
4. Forneça exemplos de uso, se possível

## ❓ Dúvidas

Se tiver dúvidas:

1. Verifique a documentação no README
2. Procure em issues fechadas
3. Abra uma nova issue com a tag "question"

## 🎓 Código de Conduta

- Seja respeitoso com todos os contribuidores
- Aceite críticas construtivas
- Foque no que é melhor para o projeto
- Mantenha um ambiente acolhedor e inclusivo

## 📚 Recursos Úteis

- [PEP 8 - Style Guide](https://pep8.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Pytest Documentation](https://docs.pytest.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

---

**Obrigado por contribuir! 🎵**
