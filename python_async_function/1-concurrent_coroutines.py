#!/usr/bin/env python 3
"""
1-concurrent_coroutines.py
"""


from typing import List
import asyncio
from basic_async_syntax import wait_random



async def wait_n(n: int, max_delay: int) -> float:
    """
    Asynchronously waits for n random delays and returns a list of the delays.
    """
    delays: List[float] = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays
