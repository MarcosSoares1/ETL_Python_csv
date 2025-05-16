import pandas as pd
df = pd.read_csv("dados.csv")

#Limpeza e transformação dos dados
# - Remover valores nulos
# - Renomear colunas
# - Criar novas colunas derivadas

df.to_csv("dados_transformados.csv", index=False) 