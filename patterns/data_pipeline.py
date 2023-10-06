import asyncio
import pandas as pd
from datetime import datetime
import requests

# Define the coroutine to remove duplicates
async def remove_duplicates(queue):
    while True:
        data = await queue.get()
        data = data.drop_duplicates()
        await queue.put(data)
        queue.task_done()

# Define the coroutine to call the 3rd party API to get coordinates
async def get_coordinates(queue):
    while True:
        data = await queue.get()
        for index, row in data.iterrows():
            address = row['Address']
            url = f'https://api.geocode.xyz/{address}?json=1'
            response = requests.get(url)
            json_response = response.json()
            data.loc[index, 'Latitude'] = json_response['latt']
            data.loc[index, 'Longitude'] = json_response['longt']
        await queue.put(data)
        queue.task_done()

# Define the function to add the import timestamp column
def add_import_timestamp(data):
    timestamp = datetime.now()
    data['Import Timestamp'] = timestamp
    return data

# Define the coroutine to process each batch of data
async def process_data(data, queue):
    # Put the initial data in the queue
    await queue.put(data)
    # Wait for all tasks to complete
    await queue.join()
    # Add the import timestamp column
    data = add_import_timestamp(data)
    return data

# Define the main function to process both batches of data asynchronously
async def main():
    # Define the two batches of data
    batch1 = pd.DataFrame({
        'Address': ['123 Main St', '456 Oak Ave', '789 Maple St', '456 Oak Ave', '234 Pine Rd']
    })
    batch2 = pd.DataFrame({
        'Address': ['345 Elm St', '678 Birch Rd', '234 Pine Rd', '910 Cedar Ln', '345 Elm St']
    })
    # Define the queue
    queue = asyncio.Queue()
    # Define the tasks to process each batch of data asynchronously
    tasks = [
        asyncio.create_task(remove_duplicates(queue)),
        asyncio.create_task(get_coordinates(queue)),
        asyncio.create_task(process_data(batch1, queue)),
        asyncio.create_task(process_data(batch2, queue))
    ]
    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)
    # Print the results
    for result in results:
        print(result)

# Run the main function
asyncio.run(main())