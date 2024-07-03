# Previsão de Estoque Inteligente com Amazon SageMaker Canvas

## Descrição

Neste guia, vou compartilhar minha experiência utilizando o Amazon SageMaker Canvas para criar um modelo de machine learning (ML) com o objetivo de prever o estoque de produtos. O processo incluiu a seleção e criação de um dataset, construção e treinamento do modelo de ML, análise do modelo e obtenção de previsões e insights.

## Etapas do Processo

### 1. Selecionar ou Criar Seu Dataset

Para iniciar, eu precisava de um dataset contendo dados relevantes para a previsão de estoque. Como não tinha dados reais disponíveis, decidi criar um dataset simulado utilizando um script em Python. O dataset incluía informações como IDs de produtos, datas de eventos, preços, indicações de promoções e quantidades em estoque.

#### Script para Criar Dataset Simulado:

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

### 2. Construção e Treinamento do ML

Com o dataset pronto, segui para o Amazon SageMaker Canvas:

1. **Importei o dataset**:
   - Fiz o upload do arquivo CSV diretamente na plataforma.

2. **Configurei o modelo**:
   - Selecionei `QUANTIDADE_ESTOQUE` como a variável alvo e incluí outras variáveis relevantes como entradas.
   - Escolhi o tipo de problema como regressão, já que eu queria prever quantidades numéricas.

3. **Construí e treinei o modelo**:
   - O SageMaker Canvas automaticamente selecionou os algoritmos mais adequados e iniciou o treinamento do modelo.

### 3. Analise do Modelo de ML

Após o treinamento do modelo, analisei os resultados fornecidos pelo SageMaker Canvas:

- **Métricas de desempenho**: A plataforma exibiu métricas como erro médio absoluto (MAE), erro quadrático médio (RMSE) e coeficiente de determinação (R²), que me ajudaram a entender a precisão do modelo.
- **Importância das características**: Identifiquei quais variáveis tinham maior impacto nas previsões, fornecendo insights sobre os fatores que influenciam o estoque.

### 4. Previsões e Insights Usando Seu Modelo de ML

Com o modelo treinado, comecei a gerar previsões e a obter insights:

1. **Realizei previsões**:
   - Utilizei o modelo para prever a quantidade de estoque futura com base em novos dados de entrada.
   - Exportei as previsões para análise adicional e tomada de decisão.

2. **Obtenção de insights**:
   - Usei os insights fornecidos pelo modelo para otimizar a gestão de estoque, identificar tendências e tomar decisões informadas.

## Conclusão

Minha experiência com o Amazon SageMaker Canvas foi bastante positiva. A plataforma facilitou a criação de um modelo preditivo robusto para previsão de estoque, mesmo sem a necessidade de um profundo conhecimento em machine learning. Seguindo estes passos, consegui desenvolver um modelo eficiente e aplicar os insights obtidos para melhorar a gestão de estoque.

Se você está interessado em explorar mais sobre o Amazon SageMaker Canvas, recomendo consultar a [documentação oficial](https://aws.amazon.com/sagemaker/canvas/).
