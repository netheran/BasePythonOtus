"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

from aiohttp import ClientSession, ClientResponse


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: ClientSession, url):
    async with session.get(url) as response:  # type: ClientResponse
        response_json = await response.json()
        return response_json


async def fetch_users_data():
    async with ClientSession() as session:
        data = await fetch_json(session, USERS_DATA_URL)  # type: dict
        return data


async def fetch_posts_data():
    async with ClientSession() as session:
        data = await fetch_json(session, POSTS_DATA_URL)  # type: dict
        return data

