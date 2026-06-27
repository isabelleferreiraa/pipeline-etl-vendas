from extract import extract_data
from transform import transform_data
from load import load_data
from logger import setup_logger

logger = setup_logger()

def main():
    logger.info("Iniciando ETL...")

    logger.info("Extraindo dados da API...")
    data = extract_data()

    logger.info("Transformando dados...")
    df = transform_data(data)

    logger.info("Salvando dados...")
    load_data(df)

    logger.info("ETL finalizado com sucesso!")

if __name__ == "__main__":
    main()