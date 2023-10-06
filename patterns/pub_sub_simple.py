import asyncio

async def publisher(queue):
    while True:
        message = input("Enter message: ")
        await queue.put(message)

async def subscriber(queue, name):
    while True:
        message = await queue.get()
        print(f"Subscriber {name} received message: {message}")

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        publisher(queue),
        subscriber(queue, "A"),
        subscriber(queue, "B"),
        subscriber(queue, "C")
    )

asyncio.run(main())