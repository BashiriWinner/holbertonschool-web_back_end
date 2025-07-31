#!/usr/bin/env python3
"""
4-tasks.py
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for n random delays and returns a list of the delays.
    """
    delays: List[float] = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays
