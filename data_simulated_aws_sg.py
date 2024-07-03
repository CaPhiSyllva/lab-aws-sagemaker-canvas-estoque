import csv
import random
from datetime import datetime, timedelta

# Função para gerar uma data aleatória no intervalo específico
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Dados para gerar o CSV
header = ["ID_PRODUTO", "DATA_EVENTO", "PRECO", "FLAG_PROMOCAO", "QUANTIDADE_ESTOQUE"]

start_date = datetime(2023, 12, 31)
end_date = datetime(2024, 7, 3)
data = []

# Gerar 1000 linhas de dados
for _ in range(1000):
    id_produto = random.randint(1000, 1024)
    data_evento = random_date(start_date, end_date).strftime("%Y-%m-%d")
    preco = round(random.uniform(10, 200), 2)
    flag_promocao = random.choice([0, 1])
    quantidade_estoque = random.randint(50, 100)
    data.append([id_produto, data_evento, preco, flag_promocao, quantidade_estoque])

# Escrever os dados no arquivo CSV
csv_file = "dados_simulados.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print(f"Arquivo CSV '{csv_file}' gerado com sucesso com 1000 linhas de dados simulados.")
