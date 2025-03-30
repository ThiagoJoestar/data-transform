import pdfplumber
import pandas as pd
import zipfile
import os

# Extrair dados da tabela do PDF
pdf_path = r"C:\Users\Pichau\Desktop\Estudos\Testes Nivelamento Intuitive Care\DataTransform\AnexoI.pdf"
# r antes da string para o Python reconhecer a \
output_csv = "Rol_de_Procedimentos.csv"
output_zip = "Teste_Thiago.zip"

# Substituições para as colunas OD e AMB
substituicoes = {
    "OD": "Odontológico",
    "AMB": "Ambulatorial"
}

# Função para processar o PDF e extrair a tabela
def extrair_dados_tabela(pdf_path):
    dados_tabela = []  # Lista para armazenar todas as linhas da tabela extraída
    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            if pagina.extract_tables():  # Verifica se há tabelas na página
                tabelas = pagina.extract_tables()
                for tabela in tabelas:
                    for linha in tabela:
                        dados_tabela.append(linha)
    return dados_tabela

# Extrair dados do PDF
print("Extraindo dados do PDF...")
dados = extrair_dados_tabela(pdf_path)

# Salvar em formato CSV
print("Processando os dados...")
df = pd.DataFrame(dados)

# Substituir abreviações pelas descrições completas
df = df.replace(substituicoes)

# Salvar como CSV
df.to_csv(output_csv, index=False, header=False)
print(f"Dados salvos em {output_csv}.")

# Compactar o CSV em um ZIP
print("Compactando os dados em um arquivo ZIP...")
with zipfile.ZipFile(output_zip, "w") as zipf:
    zipf.write(output_csv, os.path.basename(output_csv))
print(f"Arquivo compactado salvo como {output_zip}.")

# Limpar arquivo CSV temporário
os.remove(output_csv)
print("Processo concluído!")
