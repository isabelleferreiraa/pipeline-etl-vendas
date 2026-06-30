from unittest.mock import Mock, patch

import requests

from src.extract import extract_data


@patch("src.extract.requests.get")
def test_extract_data_success(mock_get):
    fake_data = [
        {
            "id": 1,
            "title": "Notebook",
            "price": 3500.00,
            "category": "electronics",
            "rating": {"rate": 4.5, "count": 120},
        }
    ]

    mock_response = Mock()
    mock_response.json.return_value = fake_data
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    data = extract_data()

    assert data == fake_data
    mock_get.assert_called_once()


@patch("src.extract.requests.get")
def test_extract_data_api_error(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException(
        "Erro na API"
    )

    import pytest

    with pytest.raises(requests.exceptions.RequestException):
        extract_data()