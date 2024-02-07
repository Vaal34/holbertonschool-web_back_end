#!/usr/bin/env python3

import random
from asyncio import sleep

async def wait_random(max_delay = 10):
    delay = random.uniform(0, max_delay)
    await sleep(delay)
    return delay
