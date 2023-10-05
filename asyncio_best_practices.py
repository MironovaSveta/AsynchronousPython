import asyncio

# Define a simple asynchronous function that simulates I/O operations
async def perform_io_operation(number):
    await asyncio.sleep(1)  # Simulate I/O delay
    print(f"IO operation {number} completed")

# Define the main function to run asynchronous tasks
async def main():
    tasks = []
    
    # Create a list of tasks for concurrent execution
    for i in range(1, 6):
        task = asyncio.create_task(perform_io_operation(i))
        tasks.append(task)
    
    # Wait for all tasks to complete using asyncio.gather
    await asyncio.gather(*tasks)

loop = asyncio.get_running_loop()
if loop and loop.is_running():
    tsk = loop.create_task(main())
    tsk.add_done_callback(
        lambda t: print(f'Task done with result={t.result()}  << return val of main()'))
else:
    print('Starting new event loop')
    result = asyncio.run(main())
