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
    """ asynchronous coroutine that waits for a random delay
        and eventually returns it
        args:
          max_delay (int): max delay
        return:
            the delay
    """
    result = random.uniform(0, max_delay)
    await asyncio.sleep(result)
    return result
