#!/usr/bin/env python3
""" write a measure_runtime coroutine that will execute
    async_comprehension four times in parallel using asyncio.gather
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ execute 4 times in parallel async_comprehension"""
    time_start = time.perf_counter()
    result = [async_comprehension() for i in range(4)]
    await asyncio.gather(*result)
    time_end = time.perf_counter()
    return (time_end - time_start)
