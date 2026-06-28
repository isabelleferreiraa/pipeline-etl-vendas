import json
import os

import requests

from config import API_URL, RAW_DATA_PATH
from logger import setup_logger

logger = setup_logger()


def extract_data():
    """
    Extrai os dados da Fake Store API e salva o JSON bruto.
    """

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Cria a pasta caso ela não exista
        os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)

        # Salva o JSON bruto
        with open(RAW_DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        logger.info("Dados extraídos da API com sucesso!")
        logger.info(f"JSON salvo em: {RAW_DATA_PATH}")

        return data

    except requests.exceptions.RequestException as e:
        logger.exception(f"Erro ao consumir a API: {e}")
        raise