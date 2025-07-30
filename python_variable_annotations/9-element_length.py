#!/usr/bin/env python3
"""
This module provides a function to compute the length of elements in a sequence.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element and its length.
    """
    return [(i, len(i)) for i in lst]
