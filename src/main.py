from extract import extract_data
from transform import transform_data
from validate import validate_data
from load import load_data
from logger import setup_logger

logger = setup_logger()


def main():
    """Executa o pipeline ETL."""

    try:
        logger.info("Iniciando ETL...")

        logger.info("Extraindo dados da API...")
        data = extract_data()

        logger.info("Transformando dados...")
        df = transform_data(data)

        logger.info("Validando dados...")
        validate_data(df)

        logger.info("Carregando dados...")
        load_data(df)

        logger.info("ETL finalizado com sucesso!")

    except Exception as e:
        logger.exception(f"Erro durante a execução do ETL: {e}")


if __name__ == "__main__":
    main()