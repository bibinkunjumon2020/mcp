# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_ollama import OllamaLLM,ChatOllama

async def main():

    server_params = StdioServerParameters(
        command="python",
        # Make sure to update to the full absolute path to your math_server.py file
        args=["my_server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            # Get tools
            tools = await load_mcp_tools(session)
            model = ChatOllama(model="qwen3:latest",verbose=True) # For faster o/p qwen3:0.6b
            # Create and run the agent
            agent = create_react_agent(model=model,tools=tools)
            agent_response = await agent.ainvoke({"messages": "what's (10 + 34 + 200) x 12 x 30 ?"})
            print(agent_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())