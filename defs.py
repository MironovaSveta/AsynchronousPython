import time

def cpu_bound_task(task):
    # Simulate a CPU-bound task (e.g., heavy computation)
    result = task * task
    time.sleep(2)
    return f"Task {task}: Result = {result}"
