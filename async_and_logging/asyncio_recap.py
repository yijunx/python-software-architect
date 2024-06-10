import asyncio
import logging
from random import randint
from typing import AsyncIterable
from http_get_functions import http_get_sync, http_get
from modern_logging.logger import logger


MAX_POKEMON = 898


def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"http://slow-server:8000/pokemons/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    logger.log(level=logging.DEBUG, msg="normal get!")
    return str(pokemon["name"])


async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"http://slow-server:8000/pokemons/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    logger.log(level=logging.DEBUG, msg="async get!")
    return str(pokemon["name"])


async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name


def normal_main() -> None:
    for _ in range(10):
        pokemon_name = get_random_pokemon_name_sync()
        print(f"{pokemon_name=}")


async def main() -> None:  # lets do it many times
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

    print(f"{result=}")


if __name__ == "__main__":
    # normal_main()
    asyncio.run(main())
