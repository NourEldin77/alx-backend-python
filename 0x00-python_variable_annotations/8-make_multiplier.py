#!/usr/bin/env python3
""" helper modules """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return function that takes float and multiply by multiplier"""
    return lambda x: x * multiplier
