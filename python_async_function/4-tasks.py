#!/usr/bin/env python3
"""Modules imported."""
import random
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for n random delays and returns a list of the delays.
    """
    delays: List[float] = []
    tasks = List[asyncio.Task] = []
    
    for _in range(n):
        tasks.append(task_wait_random(max_delay))
        
    for task in in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)
    
    return delays
