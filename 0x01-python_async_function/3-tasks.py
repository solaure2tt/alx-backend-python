#!/usr/bin/env python3
""" returns a asyncio.Task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ creat an asyncio.Task from wait_random
        args:
          max_delay (int): delays to create a task
        return:
          asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
