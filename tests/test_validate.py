import pandas as pd
import pytest

from src.validate import validate_data


def test_validate_data_success():
    df = pd.DataFrame(
        {
            "id": [1, 2],
            "title": ["Produto A", "Produto B"],
            "price": [10.5, 20.0],
            "category": ["eletronicos", "roupas"],
        }
    )

    assert validate_data(df) is True


def test_validate_empty_dataframe():
    df = pd.DataFrame()

    with pytest.raises(ValueError, match="DataFrame está vazio"):
        validate_data(df)


def test_validate_missing_columns():
    df = pd.DataFrame(
        {
            "id": [1],
            "title": ["Produto A"],
        }
    )

    with pytest.raises(ValueError, match="Colunas obrigatórias"):
        validate_data(df)


def test_validate_null_id():
    df = pd.DataFrame(
        {
            "id": [1, None],
            "title": ["Produto A", "Produto B"],
            "price": [10, 20],
            "category": ["A", "B"],
        }
    )

    with pytest.raises(ValueError, match="IDs nulos"):
        validate_data(df)


def test_validate_duplicate_id():
    df = pd.DataFrame(
        {
            "id": [1, 1],
            "title": ["Produto A", "Produto B"],
            "price": [10, 20],
            "category": ["A", "B"],
        }
    )

    with pytest.raises(ValueError, match="IDs duplicados"):
        validate_data(df)


def test_validate_null_price():
    df = pd.DataFrame(
        {
            "id": [1, 2],
            "title": ["Produto A", "Produto B"],
            "price": [10, None],
            "category": ["A", "B"],
        }
    )

    with pytest.raises(ValueError, match="preços nulos"):
        validate_data(df)


def test_validate_negative_price():
    df = pd.DataFrame(
        {
            "id": [1, 2],
            "title": ["Produto A", "Produto B"],
            "price": [10, -5],
            "category": ["A", "B"],
        }
    )

    with pytest.raises(ValueError, match="preços negativos"):
        validate_data(df)