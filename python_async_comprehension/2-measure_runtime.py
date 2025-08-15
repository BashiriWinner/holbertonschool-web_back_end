#!/usr/bin/env python3
"""measure_runtime() function"""

import asyncio
import time
from 1-async_comprehension import async_comprehension

async def measure_runtime():
    """Measures the total runtime of four async_comprehension calls"""
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
