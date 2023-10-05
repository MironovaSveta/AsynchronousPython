import asyncio
import concurrent.futures
from defs import cpu_bound_task

# Define a list of tasks (in this case, CPU-bound tasks)
tasks = [1, 2, 3, 4, 5]

async def process_tasks():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Use a ProcessPoolExecutor to run CPU-bound tasks in parallel
        loop = asyncio.get_event_loop()
        results = await asyncio.gather(*[loop.run_in_executor(executor, cpu_bound_task, task) for task in tasks])
        return results

async def main():
    results = await process_tasks()
    for result in results:
        print(result)

loop = asyncio.get_running_loop()
if loop and loop.is_running():
    tsk = loop.create_task(main())
    tsk.add_done_callback(
        lambda t: print(f'Task done with result={t.result()}  << return val of main()'))
else:
    print('Starting new event loop')
    result = asyncio.run(main())
