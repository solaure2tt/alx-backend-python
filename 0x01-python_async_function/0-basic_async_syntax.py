#!/usr/bin/env python3
"""  coroutine that takes in an integer argument
     (max_delay, with a default value of 10)
      waits for a random delay between 0 and max_delay
      seconds and eventually returns it
"""
import random
import asyncio
from typing import Generator

async def wait_random(max_delay: int = 10) -> float:
    result= random.uniform(0, max_delay)
    await asyncio.sleep(result)
    return result
