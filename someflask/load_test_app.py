
import asyncio
import requests



def http_get_sync(url: str):
    return requests.get(url).json()


async def http_get(url: str):
    return await asyncio.to_thread(http_get_sync, url)

async def visit_async_gather() -> str:
    url = f"http://localhost:5000/slow-slow-slow"
    res = await http_get(url)
    print(f"async get! {res}")
    return "gotit"


async def visit_just_loop() -> str:
    url = f"http://localhost:5000/maybe-not-so-slow"
    res = await http_get(url)
    print(f"async get! {res}")
    return "gotit"


async def load_test(x: dict) -> None:  # lets do it many times
    # pokemon_name = await get_random_pokemon_name()

    # this is one way to start 10 task at ones, with one thread
    result = await asyncio.gather(*[visit_just_loop() for _ in range(10)])

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


if __name__ == "__main__":
    asyncio.run(load_test({}))