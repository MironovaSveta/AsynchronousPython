import asyncio

async def fetch_file():
    print("Starting to fetch file")
    await asyncio.sleep(1) # duration to fetch the file
    print("Fetching file completed")

async def main():
    print("Starting main")
    await asyncio.gather(
        fetch_file(),
        fetch_file(),
        fetch_file()
    )
    print("Main completed")


loop = asyncio.get_running_loop()
if loop and loop.is_running():
    tsk = loop.create_task(main())
