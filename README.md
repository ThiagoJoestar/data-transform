# Extração de Dados de PDF para CSV

![Python](https://img.shields.io/badge/Python-3.x-blue)

## Descrição
Este projeto em Python extrai dados de tabelas presentes em um arquivo PDF e os salva em um arquivo CSV estruturado. O CSV gerado é compactado em um arquivo ZIP e algumas substituições são feitas para padronizar os dados.

## Funcionalidades
- Extração de tabelas do PDF "Anexo I".
- Salvamento dos dados extraídos em um arquivo CSV.
- Substituição de abreviações das colunas "OD" e "AMB" por suas descrições completas.
- Compactação do CSV em um arquivo ZIP.

## Tecnologias Utilizadas
- Python
- pdfplumber (para extração de dados do PDF)
- pandas (para manipulação de dados)
- zipfile (para compactação de arquivos)

## Requisitos
- Python 3.x
- Bibliotecas: pdfplumber, pandas

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Instale as dependências:
   ```bash
   pip install pdfplumber pandas
   ```

## Como Usar
1. Coloque o arquivo PDF na pasta do projeto.
2. Altere a variável `pdf_path` no código para o caminho correto do arquivo.
3. Execute o script:
   ```bash
   python DataTransform.py
   ```
4. O arquivo CSV será gerado e compactado em um ZIP com seu nome.

## Estrutura do Projeto
```
/
|-- DataTransform.py  # Script principal
|-- AnexoI.pdf        # Arquivo de entrada
|-- README.md         # Documentação
```

## Autor
Thiago Piassi  
[LinkedIn](https://linkedin.com/in/thiagopiassi)

## Licença
Este projeto está licenciado sob a MIT License.

