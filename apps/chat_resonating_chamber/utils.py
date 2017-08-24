import sys
import asyncio
from functools import partial

# async def message_received(q):
#     return await q.put(sys.stdin.readline())

#######
# OK SO SEE:
#https://github.com/calebmadrigal/asyncio-examples/blob/master/run_in_executor.py
#

# message_printing coro
async def message_vomit():
    some_message, iter_limit = await init_vomit()
    cnt = 1
    # 0 is a bad number to use cuz the `if cnt > 0` our `while True:` context will break on the 1st iteration.
    # the _iter_limit transform here assumes you'd like to have this function do something.
    _iter_limit = abs(int(iter_limit)) if iter_limit is not 0 else 1
    while True:
        # this function should take 100! seconds to execute...
        await asyncio.sleep(cnt)
        if cnt > _iter_limit:
            print('repeating {} {} times has completed.'.format(some_message, iter_limit))
            break
        print(some_message)
        cnt += 1

# NOT ASYNCHRONOUS
def write_message():
    message = input('give me a message you want to add: ')
    iter_limit = input('give me a positive integer: ')
    try:
        iter_limit = abs(int(iter_limit))
    except ValueError:
        print('INVALID ITER LIMIT ENTERED; USING DEFAULT: 100')
        iter_limit = 100
    return message, iter_limit

# transport coro
async def init_vomit(loop=None):
    # uhhhhhhh.....ok.
    if not loop:
        _loop = asyncio.get_event_loop()
    else:
        _loop = loop
    while True:
        awaitable_future = _loop.run_in_executor(None, write_message)
        return_tuple = await awaitable_future
        return return_tuple


        # new_message, iter_limit = await write_message()
        # message_future = asyncio.ensure_future(expel_vomit(new_message, iter_limit))
        # loop.create_task(message_future)
        # # await message_future


def main(loop=None):
    if not loop:
        _loop = asyncio.get_event_loop()

    else:
        _loop = loop
    try:
        loop.run_until_complete(init_vomit(loop=_loop))
    except KeyboardInterrupt:
        loop.stop()
    finally:
        loop.close()



if __name__ == '__main__':
    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolocy())
    except ImportError:
        pass
    loop = asyncio.get_event_loop()
    main(loop=loop)