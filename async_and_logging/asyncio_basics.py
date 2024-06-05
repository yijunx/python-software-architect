# the core of asyncio is a even loop
# even loop is the brain, it can do tasks, and decide what tasks to be done
# in python, 1 thread, only 1 task is done at one time
# there is no racing condition!!!

# now first, we need to understand what is coroutine and what is task
#   coroutine
#   
import asyncio


async def main():
    """i am a async func!"""
    print("hello")
    await asyncio.sleep(1)
    print("sleep is over")


async def say_after(delay, what):
    await asyncio.sleep(delay=delay)
    print(what)
    return what


async def say():
    things_to_do = [1,2,3]
    coroutines = [say_after(x, what=f"{x}s") for x in things_to_do]
    print("start")
    r = await asyncio.gather(
        *coroutines
    )
    print(f"end, {r}")

# my_coroutine = main()  # -> wont execute the code
asyncio.run(say())



