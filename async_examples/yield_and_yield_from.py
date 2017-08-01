import time
import asyncio
########################################################################################################################
# This is a non-blocking repetitive message function.
def async_repeat_message(message, interval_seconds):
    while True:
        print(message)
        start = time.time()
        expiry = start + interval_seconds
        # entering into another while loop to wait until the current time is larger than `expiry`
        while True:
            # YIELD MUST GO HERE AND NOT AT THE BOTTOM.
            yield
            now = time.time()
            if now >= expiry:
                break
########################################################################################################################
# However it could be broken up using `yield from`
def async_print_message(message, interval_seconds):
    while True:
        print(message)
        yield from async_sleep_logic(interval_seconds)

def async_sleep_logic(interval_seconds):
    start = time.time()
    expiry = start + interval_seconds
    # entering into another while loop to wait until the current time is larger than `expiry`
    while True:
        # YIELD MUST GO HERE AND NOT AT THE BOTTOM.
        yield
        now = time.time()
        if now >= expiry:
            break
########################################################################################################################
#
#       ========================
#       BUT F**K ALL THIS^ NOISE
#       ========================
#
# using the language of the times, let's modify this to obey PEP.
# Our sleep-logic is no longer necessary...(and also won't work.)
# we'll use the asyncio.sleep() function as a monkeypatch.
#
async def repeat_message(message, interval_seconds):
    while True:
        print(message)
        await asyncio.sleep(interval_seconds)


if __name__ == "__main__":
    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except ImportError:
        pass

    event_loop = asyncio.get_event_loop()

    message_A = "xXxXxXxXxXxXxXxXxXxXx"
    interval_A = 1
    message_B = "I LOVE"
    interval_B = 3
    message_C = "EXPLOSIONS!"
    interval_C = 5

    event_loop.create_task(repeat_message(message_A, interval_A))
    event_loop.create_task(repeat_message(message_B, interval_B))
    event_loop.create_task(repeat_message(message_C, interval_C))

    event_loop.run_forever()

__MODULE_OUTPUT = """
        xXxXxXxXxXxXxXxXxXxXx
        I LOVE
        EXPLOSIONS!
        xXxXxXxXxXxXxXxXxXxXx
        xXxXxXxXxXxXxXxXxXxXx
        I LOVE
        xXxXxXxXxXxXxXxXxXxXx
        xXxXxXxXxXxXxXxXxXxXx
        EXPLOSIONS!
        xXxXxXxXxXxXxXxXxXxXx
        I LOVE
        xXxXxXxXxXxXxXxXxXxXx
        xXxXxXxXxXxXxXxXxXxXx
        xXxXxXxXxXxXxXxXxXxXx
        I LOVE
        xXxXxXxXxXxXxXxXxXxXx
        EXPLOSIONS!
        xXxXxXxXxXxXxXxXxXxXx
        xXxXxXxXxXxXxXxXxXxXx
        I LOVE
        xXxXxXxXxXxXxXxXxXxXx
        xXxXxXxXxXxXxXxXxXxXx
        xXxXxXxXxXxXxXxXxXxXx
        EXPLOSIONS!
        I LOVE
        xXxXxXxXxXxXxXxXxXxXx
        xXxXxXxXxXxXxXxXxXxXx
        xXxXxXxXxXxXxXxXxXxXx
        I LOVE
        xXxXxXxXxXxXxXxXxXxXx
        xXxXxXxXxXxXxXxXxXxXx
        EXPLOSIONS!
        xXxXxXxXxXxXxXxXxXxXx
        I LOVE
        xXxXxXxXxXxXxXxXxXxXx
        xXxXxXxXxXxXxXxXxXxXx
        xXxXxXxXxXxXxXxXxXxXx
"""