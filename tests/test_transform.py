import pandas as pd

from src.transform import transform_data


def test_transform_data():
    # Dados simulando a resposta da API
    data = [
        {
            "id": 1,
            "title": "Notebook",
            "price": 2500.00,
            "category": "electronics",
            "rating": {
                "rate": 4.5,
                "count": 120
            }
        }
    ]

    df = transform_data(data)

    # Verifica se retornou um DataFrame
    assert isinstance(df, pd.DataFrame)

    # Verifica a quantidade de registros
    assert len(df) == 1

    # A coluna rating deve ter sido removida
    assert "rating" not in df.columns

    # As colunas criadas devem existir
    assert "rate" in df.columns
    assert "count" in df.columns

    # Verifica os valores
    assert df.loc[0, "rate"] == 4.5
    assert df.loc[0, "count"] == 120