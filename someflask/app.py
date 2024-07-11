from flask import Flask
import asyncio
import logging
from time import perf_counter
import requests
from modern_logging.logger import logger
from random import randint
from typing import AsyncIterable
from modern_logging.logger import logger


MAX_POKEMON = 898

app = Flask(__name__)


def http_get_sync(url: str):
    return requests.get(url).json()


async def http_get(url: str):
    return await asyncio.to_thread(http_get_sync, url)

async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"http://slow-server:8000/pokemons/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    logger.log(level=logging.DEBUG, msg="async get!")
    return str(pokemon["name"])


def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"http://slow-server:8000/pokemons/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    logger.log(level=logging.DEBUG, msg="normal get!")
    return str(pokemon["name"])


async def lolol(x: dict) -> None:  # lets do it many times
    # pokemon_name = await get_random_pokemon_name()

    # this is one way to start 10 task at ones, with one thread
    result = await asyncio.gather(*[get_random_pokemon_name() for _ in range(10)])

    # from the log, we can see it is done by a single thread and process
    # and its much faster, since get one by one normally takes 10s
    # now it is just about 1s.

    # the 1s wait is added at server side:

    # @app.route("/pokemons/<int:pokemon_id>", methods=["GET"])
    # def pokemon_endpoint(pokemon_id: int):
    #     names = ["pikachu", "bulbasaur", "charizard"]
    #     sleep(1)
    #     return {"name": names[pokemon_id % 3]}

    x["result"] = result



@app.route("/slow-slow-slow", methods=["GET"])
def pokemon_endpoint():
    result_dict = {}
    asyncio.run(lolol(result_dict))
    
    return {"stuff": result_dict}
# gunicorn someflask.app:app -w 3 --threads=100  -b 0.0.0.0:5000

@app.route("/maybe-not-so-slow", methods=["GET"])
def pokemon_endpoint_2():
    result_dict = {}
    for _ in range(10):
        pokemon_name = get_random_pokemon_name_sync()
        result_dict[pokemon_name] = "gotit"
    
    return {"stuff": result_dict}




