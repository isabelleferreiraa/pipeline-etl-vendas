import pandas as pd

from src.logger import setup_logger

logger = setup_logger()


def transform_data(data):
    """
    Transforma os dados extraídos da API em um DataFrame tratado.
    """

    try:
        # Serve para criar o DataFrame principal
        df = pd.DataFrame(data)

        # Expande a coluna 'rating' em colunas separadas
        rating_df = pd.json_normalize(df["rating"])
        df = df.drop(columns=["rating"]).join(rating_df)

        logger.info("Dados transformados com sucesso!")

        return df

    except Exception as e:
        logger.exception(f"Erro durante a transformação dos dados: {e}")
        raise