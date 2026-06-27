import os

def load_data(df):
    os.makedirs("data/processed", exist_ok=True)

    df.to_csv("data/processed/produtos_tratados.csv", index=False)