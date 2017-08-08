import asyncio
import time
from os.path import split


async def repeat_message (message, interval_seconds, max_iters=10):
    iters = 0
    while True:
        print(message)
        if iters >= max_iters:
            return 'Complete.'
        iters += 1
        await asyncio.sleep(interval_seconds)

def main():
    # Params
    message_A = "xXxXxXxXxXxXxXxXxXxXx"
    interval_A = 0.5
    message_B = "I LOVE"
    interval_B = 1
    message_C = "EXPLOSIONS!"
    interval_C = 1.5

    # Module-logic
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

    return (beginning_time, ending_time)

if __name__ == "__main__":

    name_of_module = split(__file__)[1]
    print("RUNNING MODULE: {}".format(name_of_module))
    print("\nGrandson is a follower of the philosopher Herodotus & has mastered asynchronous execution..")
    print("\nHere's the output of his module:")

    beginning_time, ending_time = main()

    pretty_beginning_time = time.asctime(time.localtime(beginning_time))
    pretty_ending_time = time.asctime(time.localtime(ending_time))
    print('\nBegun: {}\nEnded: {}\nDURATION: {} seconds'.format(pretty_beginning_time, pretty_ending_time,
                                                                (ending_time - beginning_time)))
