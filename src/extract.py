import requests

def extract_data():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    data = response.json()
    return data