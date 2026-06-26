import requests
import pandas as pd
import os
import os

os.makedirs("data", exist_ok=True)

url = "https://fakestoreapi.com/products"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

# quebrar o campo "rating"
rating_df = pd.json_normalize(df["rating"])

# juntar de volta no dataframe principal
df = df.drop(columns=["rating"]).join(rating_df)

print(df.head())

# SALVANDO O CSV (AQUI NO FINAL)
df.to_csv(os.path.join("data", "produtos_tratados.csv"), index=False)
