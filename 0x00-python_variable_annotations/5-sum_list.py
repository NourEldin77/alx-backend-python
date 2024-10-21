#!/usr/bin/env python3
""" helper modules """


from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """Return sum of list."""
    return reduce(lambda acc, crr: acc + crr, input_list, 0.0)
