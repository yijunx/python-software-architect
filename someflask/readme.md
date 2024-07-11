here is my lesson learnt

### flask endpoint using asyncio

```python
async def lolol(x: dict) -> None:
    result = await asyncio.gather(*[get_random_pokemon_name() for _ in range(10)])
    x["result"] = result


@app.route("/slow-slow-slow", methods=["GET"])
def pokemon_endpoint():
    result_dict = {}
    asyncio.run(lolol(result_dict))
    return {"stuff": result_dict}
```

run the app with 
```
gunicorn someflask.app:app -w 3 --threads=100  -b 0.0.0.0:5000
```

It works, and if we dont use the threads=100, it just do 3 requests at a time. each request makes full use of the asyncio run.

If we change to use gevent worker instead, it will complain cannot work together
```
RuntimeError: asyncio.run() cannot be called from a running event loop
```


### flask endpoint using simple loop

```python
@app.route("/maybe-not-so-slow", methods=["GET"])
def pokemon_endpoint_2():
    result_dict = {}
    for _ in range(10):
        pokemon_name = get_random_pokemon_name_sync()
        result_dict[pokemon_name] = "gotit"
    
    return {"stuff": result_dict}
```

and using a gevent worker
```
gunicorn someflask.patched_app:app -w 3 -b 0.0.0.0:5000 -k gevent
```

funny things happen. gevent start to process requests together, but in each request, it needs to go through the loop. (so all requests, are in the loop, they go in together and come out together..)

### Conclusion

i feel it is enough play with flask, for such kind of work, it is time to go to fastapi or gRPC