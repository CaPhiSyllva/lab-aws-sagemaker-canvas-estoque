# 📊 Previsão de Estoque Inteligente na AWS com [SageMaker Canvas](https://aws.amazon.com/pt/sagemaker/canvas/)

## ReadMe: Script para Gerar Dados Simulados em um Arquivo CSV

### Descrição

Este script em Python gera um arquivo CSV com 1000 linhas de dados simulados. Cada linha contém informações sobre um evento de produto, incluindo ID do produto, data do evento, preço, indicação de promoção e quantidade em estoque.

### Funcionalidades

- **Geração de Data Aleatória**: A função `random_date` gera uma data aleatória entre duas datas especificadas.
- **Dados Simulados**: Geração de dados simulados para 1000 produtos.
- **Escrita de Arquivo CSV**: Os dados simulados são escritos em um arquivo CSV.

### Estrutura do Arquivo CSV

O arquivo CSV gerado possui o seguinte cabeçalho:
- `ID_PRODUTO`: Identificador do produto (número aleatório entre 1000 e 1024)
- `DATA_EVENTO`: Data do evento (data aleatória entre 31 de dezembro de 2023 e 3 de julho de 2024)
- `PRECO`: Preço do produto (número decimal aleatório entre 10 e 200)
- `FLAG_PROMOCAO`: Indicação se o produto está em promoção (0 ou 1)
- `QUANTIDADE_ESTOQUE`: Quantidade em estoque (número aleatório entre 50 e 100)

### Como Utilizar

1. **Requisitos**:
   - Python 3.x instalado
   - Biblioteca padrão `csv` do Python

2. **Passos para Executar**:
   - Copie o script fornecido abaixo para um arquivo Python, por exemplo, `gerar_dados_simulados.py`.
   - Execute o script em um terminal ou ambiente de desenvolvimento integrado (IDE).
   - Após a execução, um arquivo chamado `dados_simulados.csv` será gerado no mesmo diretório do script.

```python
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
```

### Observações

- A função `random_date` calcula a diferença em dias entre duas datas e seleciona um número aleatório dentro desse intervalo.
- Os preços são gerados com duas casas decimais.
- A quantidade em estoque e o ID do produto são gerados dentro de intervalos especificados para garantir variedade nos dados.


Este script é útil para gerar dados de teste em cenários onde dados reais não estão disponíveis, permitindo simulações e testes de funcionalidades que dependem de dados estruturados de produtos. 

Com os dados gerados implementei no modelo de ML do SageMaker Canvas e realizei a preparação e limpeza dos dados


