import asyncio

async def foo():
    return 42


result = asyncio.run(foo())
print(result)

