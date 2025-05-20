### 📖 **README**

#### 🏆 **ETL Simples com Python e Pandas**
Este projeto implementa um pipeline ETL básico, onde extraímos dados de um arquivo CSV, realizamos transformações para limpeza e agregação de dados, e carregamos os dados tratados em um novo CSV.

### 🎖️ **Objetivo**
Demonstrar um processo ETL simples utilizando **Python e Pandas**, preparando os dados de forma organizada e aplicável para análises futuras.

### 🛠 **Ferramentas Utilizadas**
- **Python** – Linguagem principal do pipeline ETL
- **Pandas** – Manipulação e transformação de dados
- **CSV** – Formato de entrada e saída dos dados

### ⚙ **Passo a Passo do Processo**
1️⃣ **Instalação das dependências**  
   ```bash
   pip install pandas 
   ```
2️⃣ **Leitura do arquivo CSV**  
   ```python
   import pandas as pd
   df = pd.read_csv("dados_criados.csv")
   ```
3️⃣ **Limpeza e transformação dos dados**  
   - Remover valores nulos
   - Calcular Total Vendas
   - Criar novas colunas derivadas

      ```python
      import pandas as pd


      # Carregar os dados do CSV

      df = pd.read_csv("dados_criados.csv")


      # Preencher valores ausentes

      df["Preco"] = df["Preco"].fillna(df["Preco"].median())

      df["Quantidade"] = df["Quantidade"].fillna(df["Quantidade"].median())

      df["(%)Desconto"] = df["(%)Desconto"].fillna(0)


      # Calcular o total de vendas

      df["Total"] = df["Preco"] * df["Quantidade"] * (1 - df["(%)Desconto"] / 100)


      df["Total"] = df["Total"].apply(lambda x: f"R$ {x:,.2f}")

      # Salvar os dados tratados em um novo arquivo CSV

      df.to_csv("dados_tratados.csv", index=False)


      # Exibir confirmação e amostra dos dados

      print("Dados tratados e salvos em 'dados_tratados.csv'.")

      # Exibe as primeiras linhas para conferir

      print(df.head())    
     ```
      
4️⃣ **Exportação para um novo arquivo CSV**  
   ```python
   df.to_csv("dados_transformados.csv", index=False)
   ```

### 📂 **Estrutura do Repositório**
```
etl-python-csv/
│── data/
│   ├── dados_criados.csv
│── scripts/
|   ├── Principal.py
│── data/
│   ├── dados_transformados.csv  
│── README.md  
```

### 🔗 **Como Executar**
1. Clone o repositório:  
   ```bash
   git clone https://github.com/MarcosSoares1/ETL_Python_csv.git
   ```
2. Execute os scripts.


### 🤝 **Contribuições**
Sugestões e melhorias são bem-vindas! Abra uma issue ou envie um pull request.


Este é o 1° de 7 projetos para o portfolio, então sinta-se livre para contribuir. Algumas formas de contribuição além do seu exemplo de Profile README, é inserir outros utilitários na pasta [`Repositorio`](https://github.com/MarcosSoares1/ETL_Python_csv)), ou melhorar a página de pesquisa dos READMEs fazendo modificações nos arquivos da pasta [`README`]([https://github.com/](https://github.com/MarcosSoares1/ETL_Python_csv/edit/main/Readme.md). <br>
 Além disso, você também pode contribuir:
 

