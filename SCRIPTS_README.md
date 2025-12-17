# Scripts para Atualização da Apresentação

## Propósito

Estes scripts foram criados para resolver o problema de imagens não renderizarem quando o arquivo `apresentacao.html` é baixado sem a pasta de assets.

## Scripts Disponíveis

### 1. `embed_images_in_html.py`

Script principal que converte todas as imagens referenciadas no HTML para URIs de dados base64 embutidos.

**Uso:**
```bash
python3 embed_images_in_html.py
```

**O que faz:**
- Lê o arquivo `apresentacao.html`
- Encontra todas as referências a imagens com caminhos relativos
- Converte cada imagem para base64
- Substitui os caminhos relativos pelos URIs de dados base64
- Salva o arquivo HTML atualizado

### 2. `verify_embedded_images.py`

Script de verificação que confirma se todas as imagens foram corretamente embutidas.

**Uso:**
```bash
python3 verify_embedded_images.py
```

**O que faz:**
- Conta quantas imagens base64 existem no HTML
- Verifica se há caminhos relativos remanescentes
- Mostra o tamanho do arquivo
- Confirma se a conversão foi bem-sucedida

## Quando Usar

Execute estes scripts novamente se:
- Você adicionar novas imagens à apresentação
- Você atualizar imagens existentes
- Você precisar reverter para caminhos relativos e depois converter novamente

## Nota

O arquivo `apresentacao.html` atual já tem todas as imagens embutidas como base64. Não é necessário executar os scripts novamente, a menos que você faça alterações nas imagens.

## Resultado

✅ **Todas as 15 imagens únicas (21 referências totais) estão embutidas**
✅ **Tamanho do arquivo: ~15 MB**
✅ **O HTML pode ser baixado e visualizado offline com todas as imagens intactas**
