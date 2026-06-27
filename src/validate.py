def validate_data(df):
    """
    Valida o DataFrame antes do carregamento.
    """

    # Verifica se o DataFrame está vazio
    if df.empty:
        raise ValueError("O DataFrame está vazio.")

    # Colunas obrigatórias
    required_columns = [
        "id",
        "title",
        "price",
        "category"
    ]

    # Verifica se todas existem
    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Colunas obrigatórias ausentes: {missing_columns}"
        )

    # Verifica se há valores nulos na coluna "price"
    if df["price"].isnull().any():
        raise ValueError("Existem valores nulos na coluna 'price'.")

    if (df["price"] < 0).any():
        raise ValueError("Foram encontrados preços negativos.")

    return True