# -*- coding: utf-8 -*-

import asyncio
import random

async def produce(queue,n):
    for x in range(n):
        # produce an item
        print("producing {}/{}".format(x, n))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())
        item = str(x)
        # put the item in the queue
        await queue.put(item)


async def consume(queue):
    while True:
        item = await queue.get()
        print("consuming {}...".format(item))
        await asyncio.sleep(random.random())
        queue.task_done()

loop = asyncio.get_event_loop()
queue = asyncio.Queue(loop=loop)
producer = produce(queue, 10)
consumer = consume(queue)

loop.run_until_complete(asyncio.gather(producer, consumer))
loop.close()

