#!/usr/bin/env python3
from typing import List
from async_generator import async_generator  # Əvvəlki tapşırıqdan idxal

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.
    """
    

    Returns:
        List[float]: List of 10 random numbers.
    """
    return [num async for num in async_generator()]
    """
