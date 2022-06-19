import asyncio
from random import randint

from req_http import http_get, http_get_sync


MAX_POKEMON = 898


def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"http://slow-server/pokemons/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon["name"])


async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"http://slow-server/pokemons/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])


def main() -> None:
    pokemon_name = get_random_pokemon_name_sync()
    print(f"{pokemon_name=}")


