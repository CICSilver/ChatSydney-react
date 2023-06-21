import aiohttp
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

async def main():
    data = await fetch_data('https://jsonplaceholder.typicode.com/todos/1')
    print(data)

print(__name__)
#asyncio.run(main())