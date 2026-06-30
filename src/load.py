import os
import time

import psycopg2
from psycopg2.extras import execute_values

from src.config import (
    DB_HOST,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_PORT,
    PROCESSED_DATA_PATH,
)
from src.logger import setup_logger

logger = setup_logger()


def load_data(df):
    """
    Salva os dados tratados em CSV e no PostgreSQL.
    """

    # Salva o CSV tratado
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)

    conn = None
    cur = None

    try:
        # Tenta conectar ao PostgreSQL até 5 vezes
        for tentativa in range(5):
            try:
                conn = psycopg2.connect(
                    host=DB_HOST,
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    port=DB_PORT,
                )

                logger.info("Conexão com o PostgreSQL estabelecida.")
                break

            except psycopg2.OperationalError as e:
                logger.warning(
                    f"Tentativa {tentativa + 1}/5: PostgreSQL ainda não está disponível. "
                    f"Erro: {e}"
                )
                time.sleep(2)

        if conn is None:
            raise ConnectionError(
                "Não foi possível conectar ao PostgreSQL após 5 tentativas."
            )

        cur = conn.cursor()

        # Query de inserção
        query = """
            INSERT INTO produtos (id, title, price, category)
            VALUES %s
            ON CONFLICT (id) DO NOTHING;
        """

        # Prepara os dados para inserção em lote
        values = [
            (
                int(row["id"]),
                row["title"],
                float(row["price"]),
                row["category"],
            )
            for _, row in df.iterrows()
        ]

        # Insere todos os registros de uma só vez
        execute_values(cur, query, values)

        conn.commit()

        logger.info(
            f"{len(values)} registros inseridos no PostgreSQL com sucesso!"
        )

    except Exception as e:
        logger.exception(f"Erro ao carregar dados no PostgreSQL: {e}")
        raise

    finally:
        if cur:
            cur.close()

        if conn:
            conn.close()