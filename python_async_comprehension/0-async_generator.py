#!/usr/bin/env python3

"""
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""
import random
import asyncio


async def async_generator() -> float:
    """ asynchronous coroutine """
    number = random.uniform(0, 10)
    await asyncio.sleep(1)
    return number
