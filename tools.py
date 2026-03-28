from langchain_core.tools import tool
import requests


# @tool
# def get_phones_by_price_api(max_price: int):
#     """Get phones under a given price"""
#     url = "http://127.0.0.1:8000/phones/by-price"
#
#     response = requests.get(url, params={"max_price": max_price})
#
#     return response.json()


@tool
def dynamic_phone_query(sql_query: str):
    """
    Execute SQL query on phones table.

    Rules:
    - Only SELECT queries
    - Table name: phones
    - Columns: name, usd_price, battery_mah, antutu
    - Do NOT use DELETE, UPDATE, INSERT

    Example:
    SELECT name, price FROM phones WHERE price < 100000;
    """
    url = "http://127.0.0.1:8000/phones/query"

    response = requests.post(url, json={"query": sql_query})

    return response.json()