# AI MCP Smartphone Analyzer

This project demonstrates an MCP-style AI system where a language model can interact with external tools to query and analyze smartphone data.

##  Features
- Natural language queries for smartphone data
- Dynamic SQL generation using LLM
- FastAPI-based tool server (MCP-style)
- PostgreSQL database integration
- LangChain tool-calling architecture
- LangSmith tracing for observability

##  Architecture
User → LLM → Tool (API) → PostgreSQL → Response

##  Example Queries
- "Phones under 1000 with battery above 4000"
- "Best performance phones under 1500"
- "Top 5 cheapest phones"

##  Tech Stack
- LangChain (LLM + tool calling)
- FastAPI (MCP-style server)
- PostgreSQL (database)
- LangSmith (tracing & debugging)
