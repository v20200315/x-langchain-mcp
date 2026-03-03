import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
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
    async with stdio_client(stdio_server_params) as (reader, writer):
        async with ClientSession(read_stream=reader, write_stream=writer) as session:
            await session.initialize()
            print('Session initialized')
            tools = await load_mcp_tools(session)
            agent = create_agent(llm, tools)
            result = await agent.ainvoke(
                {'messages': HumanMessage(content='What is 54 + 2 * 3?')}
            )
            print(result['messages'][-1].content)


if __name__ == '__main__':
    asyncio.run(main())
