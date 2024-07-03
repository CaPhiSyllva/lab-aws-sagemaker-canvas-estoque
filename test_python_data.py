import csv
import datetime
import os

# Função para validar a geração do arquivo CSV
def testar_arquivo_csv(csv_file):
    # Verificação do arquivo
    if not os.path.exists(csv_file):
        print(f"Erro: O arquivo '{csv_file}' não foi encontrado.")
        return False
    
    # Abertura do arquivo e leitura dos dados
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        linhas = list(reader)

    # Verificação do cabeçalho
    header = ["ID_PRODUTO", "DATA_EVENTO", "PRECO", "FLAG_PROMOCAO", "QUANTIDADE_ESTOQUE"]
    if linhas[0] != header:
        print("Erro: O cabeçalho do arquivo está incorreto.")
        return False

    # Verificação do número de linhas (excluindo o cabeçalho)
    num_linhas_esperado = 1001
    if len(linhas) != num_linhas_esperado:
        print(f"Erro: O arquivo deveria ter {num_linhas_esperado} linhas, mas tem {len(linhas)}.")
        return False

    # Verificação dos tipos de dados
    for linha in linhas[1:]:
        try:
            int(linha[0])  # ID_PRODUTO
            datetime.datetime.strptime(linha[1], "%Y-%m-%d")  # DATA_EVENTO
            float(linha[2])  # PRECO
            int(linha[3])  # FLAG_PROMOCAO
            int(linha[4])  # QUANTIDADE_ESTOQUE
        except ValueError as e:
            print(f"Erro de tipo de dados na linha: {linha}\nErro: {e}")
            return False

    print(f"O arquivo '{csv_file}' foi validado com sucesso.")
    return True

# Execução do teste
csv_file = "dados_simulados.csv"
testar_arquivo_csv(csv_file)
