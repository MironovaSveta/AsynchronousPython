# Documentation

### async_main.py

##### Description:
- You define an asynchronous function called main, which serves as the main coroutine for your asynchronous code.
- You attempt to get the current running event loop using asyncio.get_running_loop(). If there is no running event loop, a RuntimeError is caught and handled by setting loop to None.
- If an event loop is already running (loop is not None and loop.is_running() returns True), you create a task from the main coroutine using loop.create_task(main()). This task represents the execution of the main coroutine on the event loop.
- You add a callback to the task using tsk.add_done_callback(). This callback function will print the result of the task when the coroutine completes.
- If there is no running event loop, you start a new one by using asyncio.run(main()), which runs the main coroutine and creates a new event loop for it.

##### Returns:
```
Async event loop already running. Adding coroutine to the event loop.
Async main
Task done with result=None  << return val of main()
```

### network_request_example.py

##### Description:
- We import the necessary modules: asyncio for asynchronous programming and aiohttp for making asynchronous HTTP requests.
- We define a list of URLs (urls) from which we want to fetch data concurrently.
- The fetch_url function is an asynchronous function that uses aiohttp to make a GET request to a URL and returns the response text if the request is successful (HTTP status code 200).
- The main function is the entry point of our program. It creates a list of tasks, each corresponding to a URL, and uses asyncio.gather to wait for all tasks to complete concurrently.

##### Returns:
```
Data from https://example.com:
<!doctype html>
<html>
<head>
    <title>Example Domain</title>
    <meta charset="utf-8" />
    <m...

Data from https://www.python.org:
<!doctype html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!-...

Data from https://github.com:
<!DOCTYPE html>
<html lang="en"   data-a11y-animated-images="system" data-a11y-link-underlines...

Task done with result=None  << return val of main()
```

### parallel_processing.py

##### Description:
- We import the necessary modules: asyncio for asynchronous programming and concurrent.futures for parallel processing of CPU-bound tasks.
- We define a list of tasks (tasks) that represents CPU-bound tasks we want to execute in parallel. In this example, we simply square each number in the list.
- The cpu_bound_task function simulates a CPU-bound task. You can replace this with your actual CPU-bound task code.
- The process_tasks function uses a concurrent.futures.ProcessPoolExecutor to run CPU-bound tasks in parallel. It creates an event loop, schedules the tasks using loop.run_in_executor, and gathers the results.
- In the main function, we run the process_tasks function asynchronously and print the results.

##### Returns:
```
Task 1: Result = 1
Task 2: Result = 4
Task 3: Result = 9
Task 4: Result = 16
Task 5: Result = 25
Task done with result=None  << return val of main()
```

### asyncio_best_practices.p

##### Description:
- We import the asyncio module for asynchronous programming.
- The perform_io_operation function is a simple asynchronous function that simulates I/O operations. It uses await asyncio.sleep(1) to simulate a 1-second I/O delay and then prints a completion message.
- The main function is the entry point of our program. It creates a list of tasks for concurrent execution using asyncio.create_task and appends them to the tasks list.
- We use asyncio.gather(*tasks) to wait for all tasks to complete concurrently. This ensures that the I/O operations run in parallel.

##### Returns:
```
Reloaded modules: defs
IO operation 1 completed
IO operation 3 completed
IO operation 5 completed
IO operation 2 completed
IO operation 4 completed
Task done with result=None  << return val of main()
```

### folder file_io/

##### Content:
- sync_file_io.py
- async_file_io.py

##### Description:
- sync_file_io.py is a Python script that demonstrates synchronous (blocking) file I/O operations. It simulates fetching a file, where each file fetch operation takes one second to complete.
- async_file_io.py is a Python script that demonstrates asynchronous (non-blocking) file I/O operations using the asyncio library. It simulates fetching a file, with each file fetch operation taking one second to complete.

##### Returns:
- sync_file_io.py
```
Starting to fetch file
Fetching file completed
Starting to fetch file
Fetching file completed
Starting to fetch file
Fetching file completed
Main completed
```
- async_file_io.py
```
Starting main
Starting to fetch file
Starting to fetch file
Starting to fetch file
Fetching file completed
Fetching file completed
Fetching file completed
Main completed
```
