#!/usr/bin/env python3
""" Measure the runtime of wait_n(n, max_delay) """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the total execution time for wait_n(n, max_delay)
        args:
          n (int): number ofrepetiotion of wait_n
          max_delay (int): max delay between executions
        return:
          total_time of execution / n
    """
    time_start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_end = time.perf_counter()
    return (time_end - time_start) / n
