import asyncio

class ChatRoom:
    def __init__(self):
        self.message_queue = asyncio.Queue()
    async def publish(self, message):
        await self.message_queue.put(message)
    async def subscribe(self, user_name):
        while True:
            message = await self.message_queue.get()
            print(f"{user_name} received message: {message}")

async def main():
    chat_room = ChatRoom()
    await asyncio.gather(
        chat_room.publish("Hello, world!"),
        chat_room.subscribe("Alice"),
        chat_room.subscribe("Bob")
    )

asyncio.run(main())