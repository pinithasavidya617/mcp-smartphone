from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from tools import get_phones_by_price_api
import os

load_dotenv()

def make_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    tools = [get_phones_by_price_api]

    llm_with_tools = llm.bind_tools(tools)

    return llm_with_tools, tools