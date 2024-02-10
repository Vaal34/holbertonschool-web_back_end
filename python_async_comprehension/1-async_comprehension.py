#!/usr/bin/env python3
async_generator = __import__('0-async_generator').async_generator
"""
Import async_generator from the previous task and then write
a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an
async comprehensing over async_generator,
then return the 10 random numbers.
"""
import typing


async def async_comprehension() -> typing.List[float]:
    """ function that create a list à to 10 with async comprehension """
    return [data async for data in async_generator()]
