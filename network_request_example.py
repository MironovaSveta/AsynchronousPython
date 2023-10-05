import asyncio
import aiohttp

# List of URLs to fetch data from
urls = ["https://example.com", "https://www.python.org", "https://github.com"]

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Ensure the response is successful (HTTP status code 200)
            if response.status == 200:
                return await response.text()
            else:
                return None

async def main():
    # Create a list of tasks for fetching data from each URL
    tasks = [fetch_url(url) for url in urls]
    
    # Wait for all tasks to complete concurrently
    results = await asyncio.gather(*tasks)
    
    # Process the results
    for url, result in zip(urls, results):
        if result:
            print(f"Data from {url}:\n{result[:100]}...\n")

loop = asyncio.get_running_loop()
if loop and loop.is_running():
    tsk = loop.create_task(main())
    tsk.add_done_callback(
        lambda t: print(f'Task done with result={t.result()}  << return val of main()'))
else:
    print('Starting new event loop')
    result = asyncio.run(main())
