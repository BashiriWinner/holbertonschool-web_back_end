#!/usr/bin/env python3
"""async_generator() function"""


from typing import Generator
import asyncio
import random


async def async_generator()-> Generator[float, None, None]:
    
    """An asynchronous generator that yields 10 random float values"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
