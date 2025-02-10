# TPC1 - Removedor de Linhas Duplicadas

## Descrição
Este script Python fornece uma ferramenta de linha de comando para remover linhas duplicadas de um arquivo de texto, com a opção adicional de contabilizar e exibir o número de ocorrências de cada linha.

## Funcionalidades
- Remove linhas duplicadas de um arquivo de texto
- Opção para mostrar o número de repetições de cada linha
- Suporta saída para arquivo ou para o terminal (stdout)
- Tratamento de erros para problemas de I/O

## Requisitos
- Python 3.x

## Uso
```bash
python script.py arquivo_entrada [arquivo_saida] [--count]
```

### Argumentos
- `arquivo_entrada`: Caminho para o arquivo de entrada (obrigatório)
- `arquivo_saida`: Caminho para o arquivo de saída (opcional)
- `--count` ou `-c`: Adiciona o número de repetições antes de cada linha

### Exemplos
1. Remover duplicatas e mostrar no terminal:
```bash
python script.py input.txt
```

2. Remover duplicatas e salvar em novo arquivo:
```bash
python script.py input.txt output.txt
```

3. Remover duplicatas e mostrar contagem de repetições:
```bash
python script.py input.txt --count
```