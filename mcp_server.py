from fastapi import FastAPI
from pydantic import BaseModel

from db import get_connection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MCP Server Running"}

class SQLQuery(BaseModel):
    query: str


# @app.get("/phones/by-price")
# def get_phones_by_price(max_price: int):
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     cursor.execute(
#         "SELECT name, usd_price, battery_mah FROM phones WHERE usd_price <= %s",
#         (max_price,)
#     )
#
#     results = cursor.fetchall()
#
#     cursor.close()
#     conn.close()
#
#     return {"phones": results}

@app.post("/phones/query")
def query_phones(data : SQLQuery):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(data.query)
        results = cursor.fetchall()

        return {"result": results}

    except Exception as e:
        return {"error": str(e)}

    finally:
        cursor.close()
        conn.close()