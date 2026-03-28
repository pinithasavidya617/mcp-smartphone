from fastapi import FastAPI
from db import get_connection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MCP Server Running"}


@app.get("/phones/by-price")
def get_phones_by_price(max_price: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, usd_price, battery_mah FROM phones WHERE usd_price <= %s",
        (max_price,)
    )

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"phones": results}