import time
from os.path import split

def blocking_repeat_message(message, interval_seconds, max_iters=10):
    iters = 0
    while True:
        print(message)
        if iters >= max_iters:
            break
        iters += 1
        time.sleep(interval_seconds)

if __name__ == '__main__':
    message_A = "xXxXxXxXxXxXxXxXxXxXx"
    interval_A = 0.5
    message_B = "I LOVE"
    interval_B = 1
    message_C = "EXPLOSIONS!"
    interval_C = 1.5

    print("RUNNING MODULE: {}\n\nGrandpa doesn't know anything about asynchronous execution.\n\nHere's the output of his module:".format(split(__file__)[1]))

    beginning_time = time.time()

    blocking_repeat_message(message_A, interval_A)
    blocking_repeat_message(message_B, interval_B)
    blocking_repeat_message(message_C, interval_C)

    ending_time = time.time()

    pretty_beginning_time = time.asctime(time.localtime(beginning_time))
    pretty_ending_time = time.asctime(time.localtime(ending_time))
    print('\nBegun: {}\nEnded: {}\nDURATION: {} seconds'.format(pretty_beginning_time, pretty_ending_time, (ending_time - beginning_time)))
