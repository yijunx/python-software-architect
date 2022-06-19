from time import sleep
from flask import Flask


app = Flask(__name__)


@app.route("/slow_endpoint", methods=["GET"])
def slow_response():
    sleep(10)
    return {"result": 0}

@app.route("/pokemons/<int:pokemon_id>", methods=["GET"])
def pokemon_endpoint(pokemon_id: int):
    names = ["pikachu", "bulbasaur", "charizard"]
    sleep(1)
    return {"name": names[pokemon_id % 3]}