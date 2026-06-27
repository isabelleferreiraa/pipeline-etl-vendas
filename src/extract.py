import requests

from config import API_URL
from logger import setup_logger

logger = setup_logger()


def extract_data():
    """
    Extrai os dados da Fake Store API.
    """

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        logger.info("Dados extraídos da API com sucesso!")

        return response.json()

    except requests.exceptions.RequestException as e:
        logger.exception(f"Erro ao consumir a API: {e}")
        raise