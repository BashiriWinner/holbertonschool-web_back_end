#!/usr/bin/env python3
"""
This module provides a function to convert a key-value pair into a tuple.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key-value pair into a tuple where the value is squared.
    """
    return(k, (v * v))
