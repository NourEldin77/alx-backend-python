#!/usr/bin/env python3
""" helper modules """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return sum of list."""
    return (k, float(v ** 2))
