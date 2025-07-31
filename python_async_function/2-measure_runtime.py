#!/usr/bin/env python3
"""
2-measure_runtime.py
"""


import asyncio
import typing from list
import time

measure_time = __import__('2-measure_runtime').measure_time


async def measure_time(n: int, max_delay: int) -> float:
    """
    Asynchronously measures the average time taken to run wait_n.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
