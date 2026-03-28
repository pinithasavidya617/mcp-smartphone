from langchain_core.tools import tool
import requests


@tool
def get_phones_by_price_api(max_price: int):
    """Get phones under a given price"""
    url = "http://127.0.0.1:8000/phones/by-price"

    response = requests.get(url, params={"max_price": max_price})

    return response.json()