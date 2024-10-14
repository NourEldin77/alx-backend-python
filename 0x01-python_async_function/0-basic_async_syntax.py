#!/usr/bin/env python3
""" function wati_random """


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    @param: max_delay (sleep)
    Return - random value sleeped
    """
    random_value = random.uniform(0, max_delay)
    await asyncio.sleep(random_value)
    return random_value
