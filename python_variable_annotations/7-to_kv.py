#!/usr/bin/env python3
from typing import Tuple, Union

def to_kv(k: str, v: Tuple(Optional(int OR float))) -> float:
    return(v, float(v * v))
