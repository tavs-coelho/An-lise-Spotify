# Política de Segurança

## Versões Suportadas

Lançamos patches para vulnerabilidades de segurança. Versões atualmente suportadas:

| Versão  | Suportada          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reportando uma Vulnerabilidade

Levamos a segurança do nosso projeto a sério. Se você descobrir uma vulnerabilidade de segurança, por favor siga estes passos:

### 1. Não Divulgue Publicamente

Por favor, não divulgue publicamente a vulnerabilidade até que tenhamos tido a chance de resolvê-la.

### 2. Entre em Contato

Reporte vulnerabilidades de segurança por:
- Abrir um GitHub Security Advisory
- Enviar um e-mail aos mantenedores através do GitHub

### 3. Forneça Detalhes

Inclua as seguintes informações:
- Descrição da vulnerabilidade
- Passos para reproduzir
- Impacto potencial
- Correção sugerida (se houver)

### 4. Cronograma de Resposta

- **Resposta Inicial:** Dentro de 48 horas
- **Atualização de Status:** Dentro de 7 dias
- **Cronograma de Correção:** Depende da severidade
  - Crítica: Dentro de 7 dias
  - Alta: Dentro de 14 dias
  - Média: Dentro de 30 dias
  - Baixa: Melhor esforço

## Melhores Práticas de Segurança

Ao usar este projeto:

1. **Mantenha Dependências Atualizadas:** Atualize regularmente todas as dependências
2. **Use Ambientes Virtuais:** Isole as dependências do projeto
3. **Revise o Código:** Sempre revise o código antes de executar
4. **Segurança da API:** Use HTTPS em produção, implemente rate limiting
5. **Variáveis de Ambiente:** Nunca commite secrets ou chaves de API
6. **Validação de Entrada:** Sempre valide entradas de usuário
7. **Segurança Docker:** Use tags de versão específicas, não `latest`

## Funcionalidades de Segurança

Este projeto inclui:

- ✅ Scan de segurança com Bandit
- ✅ Verificação de segurança de dependências com Safety
- ✅ Verificações de qualidade de código com flake8
- ✅ Verificação de tipos com mypy
- ✅ Verificações automáticas de segurança CI/CD
- ✅ Permissões mínimas de GITHUB_TOKEN
- ✅ Validação de entrada com Pydantic

## Divulgação Responsável

Apreciamos divulgação responsável e reconheceremos contribuidores que reportarem vulnerabilidades, a menos que prefiram permanecer anônimos.

Obrigado por ajudar a manter este projeto seguro!
