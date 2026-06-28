import logging
import os


def setup_logger():
    """
    Configura e retorna o logger da aplicação.
    """

    logger = logging.getLogger("ETL")

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Cria a pasta de logs caso ela não exista
    os.makedirs("logs", exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler(
        os.path.join("logs", "pipeline.log"),
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger