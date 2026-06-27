import os
import psycopg2

from config import (
    DB_HOST,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_PORT,
    PROCESSED_DATA_PATH,
)
from logger import setup_logger

logger = setup_logger()


def load_data(df):
    """
    Salva os dados tratados em CSV e no PostgreSQL.
    """

    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)

    conn = None
    cur = None

    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
        )

        cur = conn.cursor()

        for _, row in df.iterrows():
            cur.execute(
                """
                INSERT INTO produtos (id, title, price, category)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
                """,
                (
                    int(row["id"]),
                    row["title"],
                    float(row["price"]),
                    row["category"],
                ),
            )

        conn.commit()
        logger.info("Dados carregados no PostgreSQL com sucesso!")

    except Exception as e:
        logger.exception(f"Erro ao carregar dados no PostgreSQL: {e}")
        raise

    finally:
        if cur:
            cur.close()

        if conn:
            conn.close()