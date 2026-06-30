import os

from dotenv import load_dotenv

load_dotenv()

# API
API_URL = "https://fakestoreapi.com/products"

# Caminhos dos arquivos
RAW_DATA_PATH = "data/raw/produtos_raw.json"
PROCESSED_DATA_PATH = "data/processed/produtos_tratados.csv"

# Banco de dados
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
