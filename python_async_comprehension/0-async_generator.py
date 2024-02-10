#!/usr/bin/env python3

"""
Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and
max_delay (included and float value) seconds and eventually returns it.
"""
import random
import asyncio


async def async_generator() -> float:
    """ asynchronous coroutine """
    number = random.uniform(0, 10)
    await asyncio.sleep(1)
    return number
