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