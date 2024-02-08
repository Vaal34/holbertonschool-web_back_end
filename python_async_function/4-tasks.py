#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve written and
write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """ return the list of all the delays """
    result = [task_wait_random(max_delay) for i in range(n)]
    return sorted(await asyncio.gather(*result))
