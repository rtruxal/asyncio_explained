import asyncio
import time
from os.path import split

async def repeat_message(message, interval_seconds, max_iters=10):
    iters = 0
    while True:
        print(message)
        if iters >= max_iters:
            return 'Complete.'
        iters += 1
        await asyncio.sleep(interval_seconds)


if __name__ == "__main__":
    message_A = "xXxXxXxXxXxXxXxXxXxXx"
    interval_A = 0.5
    message_B = "I LOVE"
    interval_B = 1
    message_C = "EXPLOSIONS!"
    interval_C = 1.5

    print("RUNNING MODULE: {}\n\nGrandson is a follower of the philosopher Herodotus & has mastered asynchronous execution.\n\nHere's the output of his function:".format(split(__file__)[1]))

    beginning_time = time.time()

    event_loop = asyncio.get_event_loop()

    task_A = event_loop.create_task(repeat_message(message_A, interval_A))
    task_B = event_loop.create_task(repeat_message(message_B, interval_B))
    task_C = event_loop.create_task(repeat_message(message_C, interval_C))

    try:
        event_loop.run_until_complete(asyncio.gather(task_A, task_B, task_C))
    finally:
        event_loop.close()

    ending_time = time.time()

    pretty_beginning_time = time.asctime(time.localtime(beginning_time))
    pretty_ending_time = time.asctime(time.localtime(ending_time))
    print('\nBegun: {}\nEnded: {}\nDURATION: {} seconds'.format(pretty_beginning_time, pretty_ending_time,
                                                                (ending_time - beginning_time)))
