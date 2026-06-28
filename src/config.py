import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

PROCESSED_DATA_PATH = "data/processed/produtos_tratados.csv"
API_URL = "https://fakestoreapi.com/products"
RAW_DATA_PATH = "data/raw/produtos_raw.json"