import asyncio

# Define an asynchronous function called 'main'
async def main():
    print("Async main")

try:
    # Attempt to get the current running event loop
    loop = asyncio.get_running_loop()
except RuntimeError:  
    # Handle the case when there is no current event loop
    loop = None

if loop and loop.is_running():
    # If an event loop is already running, add the 'main' coroutine to it
    print('Async event loop already running. Adding coroutine to the event loop.')
    
    # Create a task from the 'main' coroutine and schedule it on the event loop
    tsk = loop.create_task(main())
    
    # Add a callback to print the result when the coroutine completes
    tsk.add_done_callback(
        lambda t: print(f'Task done with result={t.result()}  << return val of main()'))
else:
    # If there is no running event loop, start a new one
    print('Starting a new event loop')
    
    # Run the 'main' coroutine using asyncio.run() to start a new event loop
    result = asyncio.run(main())
