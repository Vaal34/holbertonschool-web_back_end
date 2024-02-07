#!/usr/bin/env python3
import asyncio
import typing

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> typing.List[float]:

    result = [wait_random(max_delay) for i in range(n)]
    return sorted(await asyncio.gather(*result))