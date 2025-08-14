#!/usr/bin/env python3
"""async_comprehension() function"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random float values from an asynchronous generator"""
    return [num async for num in async_generator()]
