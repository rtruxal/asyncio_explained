import asyncio
__doc__ = """
3 sections showing the evolution of what is now referred to as `await` in the stdlib.
"""

########################################################################################################################
def generator_A1():
    yield 'b'
    yield 'c'
    yield 'd'

def generator_A2():
    yield 'A'
    for letter in generator_A1():
        yield letter
    yield 'E'
    yield 'F'
#--------------------------------------------

def test_A():
    for i in generator_A2():
        print(i)

########################################################################################################################
def generator_B1():
    yield 'b'
    yield 'c'
    yield 'd'

def generator_B2():
    yield 'A'
    yield from generator_B1()
    yield 'E'
    yield 'F'
#--------------------------------------------

def test_B():
    for i in generator_B2():
        print(i)

########################################################################################################################
async def async_generator_spits_out_letters():
    yield 'a'
    yield 'b'
    yield 'd'
    yield 'c'


async def async_generator_C2():
    ## CLOSE, BUT NO CIGAR:
    # return (await async_generator_spits_out_letters())
    ## THIS ONE:
    return [i async for i in async_generator_spits_out_letters()]


#random coroutine
async def coroutine_prints_messages():
    while True:
        print('hi')
        await asyncio.sleep(2)

#--------------------------------------------

def test_C():
    # print(type(async_generator_C2()))
    print(type(async_generator_spits_out_letters()))
    print(type(coroutine_prints_messages()))
    print()
    # print(type(async_generator_C2))
    print(type(async_generator_spits_out_letters))
    print(type(coroutine_prints_messages))
    # loop = asyncio.get_event_loop()
    # ans = loop.run_until_complete(async_generator_C2())
    # loop.close()
    # return ans

def loopit():
    loop = asyncio.get_event_loop()
    print(type(loop))
    # coro_message_print = loop.create_task(coroutine_prints_messages())
    # async_gen_yield_lets = loop.create_task(async_generator_spits_out_letters())
    # loop.run_until_complete(asyncio.gather(coro_message_print, async_gen_yield_lets))
    # loop.close()


if __name__ == '__main__':
    # test_A()
    # test_B()
    # test_C()
    loopit()
