import requests
import asyncio


def http_get_sync(url: str):
    return requests.get(url).json()


async def http_get(url: str):
    return await asyncio.to_thread(http_get_sync, url)
