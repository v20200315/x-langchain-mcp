import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

stdio_server_params = StdioServerParameters(
    command='python',
    args=[
        '/Users/victor/myfolder/workspace-cursor/x-langchain-mcp/servers/math_server.py'
    ],
)


async def main():
    print('Hello from x-langchain-mcp!')


if __name__ == '__main__':
    asyncio.run(main())
