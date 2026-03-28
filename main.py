from agent import make_agent

def main():
    llm, tools = make_agent()

    while True:
        query = input("Ask: ")

        response = llm.invoke(query)

        #  Check if tool is called
        if response.tool_calls:
            for tool_call in response.tool_calls:
                tool_name = tool_call["name"]
                args = tool_call["args"]

                # Find matching tool
                for tool in tools:
                    if tool.name == tool_name:
                        result = tool.invoke(args)

                        # Send result back to LLM
                        final_response = llm.invoke(
                            f"""
                            User asked: {query}\nTool result: {result}
                            Explain this nicely and recommend best options
                            """
                        )

                        print("Answer:", final_response.content)
        else:
            print("Answer:", response.content)
            print("Tool calls:", response.tool_calls)


if __name__ == "__main__":
    main()