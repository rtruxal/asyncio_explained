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

    blocking_repeat_message(message_A, interval_A)
    blocking_repeat_message(message_B, interval_B)
    blocking_repeat_message(message_C, interval_C)

    ending_time = time.time()

    return (beginning_time, ending_time)

if __name__ == '__main__':
    # begin_time, end_time = main()
    # duration = end_time - begin_time
    # print("Execution time in seconds: {}".format(duration))


    ## Print-logic
    name_of_module = split(__file__)[1]
    print("RUNNING MODULE: {}".format(name_of_module))
    print("\nGrandpa doesn't know anything about asynchronous execution.")
    print("\nHere's the output of his module:")

    beginning_time, ending_time = main()

    pretty_beginning_time = time.asctime(time.localtime(beginning_time))
    pretty_ending_time = time.asctime(time.localtime(ending_time))
    print('\nBegun: {}\nEnded: {}\nDURATION: {} seconds'.format(pretty_beginning_time,
                                                                pretty_ending_time,
                                                                (ending_time - beginning_time)))
