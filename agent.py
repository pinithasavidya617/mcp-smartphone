from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
# from tools import get_phones_by_price_api
from tools import dynamic_phone_query
import os

load_dotenv()

def make_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    tools = [dynamic_phone_query]

    llm_with_tools = llm.bind_tools(tools)

    return llm_with_tools, tools