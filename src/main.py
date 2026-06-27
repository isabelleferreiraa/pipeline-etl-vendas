import sys
import importlib

from extract import extract_data
from transform import transform_data
from logger import setup_logger
from validate import validate_data
import load  # mantém import normal

logger = setup_logger()

def main():

    try:
        print("🔥 ESTOU RODANDO O MAIN.PY DE src")

        # 🔍 DEBUG DO MÓDULO
        print("📦 LOAD ESTÁ EM:")
        print(load.__file__)

        print("📦 PYTHON PATH (resumo):")
        print(sys.path[:3])

        logger.info("Iniciando ETL...")

        logger.info("Extraindo dados da API...")
        data = extract_data()

        logger.info("Transformando dados...")
        df = transform_data(data)

        print("👉 DATA PRONTO:", type(data))
        print("👉 DF PRONTO:", type(df))

        logger.info("Validando dados...")
        validate_data(df)

        logger.info("➡️ VOU CHAMAR O LOAD AGORA")
        print("🔥 DEBUG: chamando load.load_data(df)")

        # 🚀 chamada direta
        load.load_data(df)

        logger.info("✔ LOAD FINALIZADO")
        logger.info("ETL finalizado com sucesso!")

    except Exception as e:
        logger.exception(f"Erro durante a execução do ETL: {e}")

if __name__ == "__main__":
    main()