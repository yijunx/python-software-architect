import asyncio


async def main():
    # just await
    # await asyncio.sleep(0.1)

    # using create task
    await asyncio.create_task(
        asyncio.sleep(0.1)
    )


asyncio.run(main())