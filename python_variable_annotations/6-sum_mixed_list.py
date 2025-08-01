#!/usr/bin/env python3
"""
This module provides a function to sum a mixed list of integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a mixed list of integers and floats.
    """
    return sum(mxd_lst)
