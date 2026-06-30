from unittest.mock import Mock, patch

import pandas as pd
import psycopg2
import pytest

from src.load import load_data


@patch("src.load.execute_values")
@patch("src.load.psycopg2.connect")
def test_load_data_success(mock_connect, mock_execute_values):
    """
    Testa se os dados são carregados corretamente no PostgreSQL.
    """

    df = pd.DataFrame(
        {
            "id": [1, 2],
            "title": ["Produto A", "Produto B"],
            "price": [10.5, 20.0],
            "category": ["A", "B"],
        }
    )

    # Mock da conexão
    mock_conn = Mock()
    mock_cursor = Mock()

    mock_conn.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_conn

    load_data(df)

    # Verifica se conectou ao banco
    mock_connect.assert_called_once()

    # Verifica se abriu cursor
    mock_conn.cursor.assert_called_once()

    # Verifica se executou a inserção em lote
    mock_execute_values.assert_called_once()

    # Verifica se realizou commit
    mock_conn.commit.assert_called_once()

    # Verifica se fechou cursor e conexão
    mock_cursor.close.assert_called_once()
    mock_conn.close.assert_called_once()


@patch("src.load.time.sleep", return_value=None)
@patch("src.load.psycopg2.connect")
def test_load_connection_error(mock_connect, mock_sleep):
    """
    Testa se a função lança ConnectionError após
    falhar nas 5 tentativas de conexão.
    """

    mock_connect.side_effect = psycopg2.OperationalError()

    df = pd.DataFrame(
        {
            "id": [1],
            "title": ["Produto"],
            "price": [10],
            "category": ["A"],
        }
    )

    with pytest.raises(ConnectionError):
        load_data(df)

    # Deve tentar conectar 5 vezes
    assert mock_connect.call_count == 5

    # Deve esperar entre as tentativas
    assert mock_sleep.call_count == 5