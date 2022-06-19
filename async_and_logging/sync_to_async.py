import asyncio
import logging
from time import perf_counter
import requests
from logger import logger


async def counter(until: int = 15):
    now = perf_counter()
    logger.log(level=logging.DEBUG, msg="Start counter!")

    for i in range(0, until):
        last = now
        await asyncio.sleep(0.1)
        now = perf_counter()
        logger.log(level=logging.DEBUG, msg=f"{i}: was asleep for {now - last}s")


def send_request(url: str):
    logger.log(level=logging.DEBUG, msg="Sending HTTP request")
    return requests.get(url).status_code


async def send_async_request(url: str):
    return await asyncio.to_thread(send_request, url)


async def main():
    # first method
    task = asyncio.create_task(counter())
    status_code = await send_async_request("http://slow-server:8000/pokemons/13")
    # log the HTTP request without waiting for counter to finish
    logger.log(level=logging.DEBUG, msg=f"HTTP RESPONSE WITH STATUS {status_code}")
    await task

    # # second
    # # another way to write this with gather
    # status_code, _ = await asyncio.gather(
    #     send_async_request("http://slow-server:8000/pokemons/13"), counter()
    # )
    # # but now it only reports the HTTP response wafter counter finish!
    # logger.log(level=logging.DEBUG, msg=f"HTTP RESPONSE WITH STATUS {status_code}")

# log is intesting, we get the response while the counter is running! (first method)
# yijunx@0bd436b7eaba:~/code$ python async_and_logging/sync_to_async.py 
# logger:2022-06-19 14:34:02,540:DEBUG:MSG-Sending HTTP request:PROCESS-7463:THREAD-139936623613696
# logger:2022-06-19 14:34:02,541:DEBUG:MSG-Start counter!:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:02,645:DEBUG:MSG-0: was asleep for 0.10383546695811674s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:02,747:DEBUG:MSG-1: was asleep for 0.1020956480060704s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:02,848:DEBUG:MSG-2: was asleep for 0.10158859303919598s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:02,950:DEBUG:MSG-3: was asleep for 0.10131669900147244s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:03,052:DEBUG:MSG-4: was asleep for 0.10188316297717392s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:03,154:DEBUG:MSG-5: was asleep for 0.10200844897190109s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:03,255:DEBUG:MSG-6: was asleep for 0.10145126801216975s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:03,357:DEBUG:MSG-7: was asleep for 0.10163566202390939s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:03,459:DEBUG:MSG-8: was asleep for 0.10205831896746531s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:03,560:DEBUG:MSG-HTTP RESPONSE WITH STATUS 200:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:03,561:DEBUG:MSG-9: was asleep for 0.10190085001522675s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:03,662:DEBUG:MSG-10: was asleep for 0.10162166098598391s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:03,764:DEBUG:MSG-11: was asleep for 0.10156665201066062s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:03,866:DEBUG:MSG-12: was asleep for 0.10170697799185291s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:03,967:DEBUG:MSG-13: was asleep for 0.10149193101096898s:PROCESS-7463:THREAD-139936641685312
# logger:2022-06-19 14:34:04,069:DEBUG:MSG-14: was asleep for 0.10152014199411497s:PROCESS-7463:THREAD-139936641685312


asyncio.run(main())
