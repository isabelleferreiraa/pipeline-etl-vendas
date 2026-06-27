from logger import setup_logger

logger = setup_logger()


def validate_data(df):
    """
    Valida o DataFrame antes do carregamento.
    """

    if df.empty:
        raise ValueError("O DataFrame está vazio.")

    required_columns = [
        "id",
        "title",
        "price",
        "category",
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Colunas obrigatórias ausentes: {missing_columns}"
        )

    if df["id"].isnull().any():
        raise ValueError("Existem IDs nulos.")

    if df["id"].duplicated().any():
        raise ValueError("Existem IDs duplicados.")

    if df["price"].isnull().any():
        raise ValueError("Existem preços nulos.")

    if (df["price"] < 0).any():
        raise ValueError("Existem preços negativos.")

    logger.info("Validação concluída com sucesso!")

    return True