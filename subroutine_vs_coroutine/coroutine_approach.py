import asyncio

async def sum_numbers_coroutine(numbers):
    total = 0
    for num in numbers:
        total += num
        await asyncio.sleep(0)  # Yield control to the event loop briefly
    return total

async def main():
    numbers = [1, 2, 3, 4, 5]
    result = await sum_numbers_coroutine(numbers)
    print("Sum of numbers (coroutine):", result)

loop = asyncio.get_running_loop()
if loop and loop.is_running():
    tsk = loop.create_task(main())