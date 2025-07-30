#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(x: float) -> float:
        return x * multiplier
        """
        Multiplies the input by the multiplier.
        """
    return multiplier_function
