from itertools import islice
__doc__ = """
This is a 'simple' example of how python3 runs jobs asynchronously.

Fundamental concepts:
    - `asyncio` loops create coroutines by exploiting the following behavior of NON-BLOCKING functions.
        - they are state-saving.
        - they produce callable objects.
        
    - What is a NON-BLOCKING function?
        - GENERATOR functions contain a yield statement.
        - BLOCKING functions contain a return statement.
        - NON-BLOCKING functions contain BOTH a yield AND return statement.
            - non-blocking functions MUST ALWAYS call yield at least 1 time.
    
    - How do these loops do this?
        - With something called a Scheduler. 
            - It's basically a fancy queue.
        - We will get to this topic in `emulating_async_classes_with_stdlib.py`

    - Why do I need to monkeypatch so friggin' much?
        - Clearly you already know a bit about this.
        - We will get to this topic in `yield_and_yield_from.py`
"""
# A)
def fibb():
    # This is an infinitely recursive sequence-generator.
    yield 1
    a = 1
    b = 1
    while True:
        yield b
        a, b = b, a + b

# B) (ALL PREDICATES MUST BE FUNCTIONS THAT EVALUATE TO TRUE/FALSE.)
def make_predicate(positive_integer):
    # input: positive int
    # output: a length-checker function
    return lambda x: len(str(x)) >= positive_integer

# C)
def blocking_numba_search(iterable, predicate):
    # This is a typical iterable function, containing a `return` but no `yield`.
    # It has no concept of state & must be run all at once.
    for item in iterable:
        if predicate(item):
            return item
            # yield 'Searching...'
    return ValueError("val not found.")

# D)
def async_numba_search(iterable, predicate):
    # The addition of `yield` after each iteration MAKES THIS FUNCTION NON-BLOCKING.
    for item in iterable:
        if predicate(item):
            return item
        yield 'Searching...'
    return ValueError("val not found.")


if __name__ == "__main__":

    thin_line = '-'*64
    thick_line = '='*64
    hash_line = '#'*64

# A) fibb()
    print(hash_line)
    print('testing our infinite-recursive sequence generator func.')
    print('islice says "give me 20 vals from the generator."')
    print(thick_line)
    print('OUTPUT: {}'.format(list(islice(fibb(), 20))))

    print(hash_line)
    print('\n')
    print(hash_line)

# B) make_predicate()
    print('make_predicate should always produce a conditional check-function')
    print('in this case, it is looking for a number with `n` "figures"')
    print(thick_line)
    sequence = [1, 20, 300, 4000, 50000]
    n = 3
    print('n == {}'.format(n))
    print('sequence == {}'.format(sequence))
    print(thin_line)
    print('is_there_a_number_longer_than_n_digits = make_predicate(n)')
    is_there_a_number_longer_than_n_digits = make_predicate(n)
    print('is_there_a_number_longer_than_n_digits(sequence)')
    print('OUTPUT: {}'.format(is_there_a_number_longer_than_n_digits(sequence)))
    # this produces the function:
    #    lambda x: len(str(x)) >= n      #<=(here n == 3)

    print(hash_line)
    print('\n')
    print(hash_line)

#C) blocking_numba_search()
    print('Testing our normal search function.')
    print('your return statement will stop the function.')
    print(thick_line)
    print('blocking_numba_search(fibb(), make_predicate(3))')
    print('OUTPUT: {}'.format(blocking_numba_search(fibb(), make_predicate(3))))

    print(hash_line)
    print('\n')
    print(hash_line)

#D) async_numba_search()
    print('A blocking-function can be turned into an async function by')
    print('adding yield inside the iteration.')
    print(thin_line)
    print('Note that I can inject arbitrary jobs as I continue to call next.')
    print('This is the behavior exploited to do ALL async things.')
    print(thick_line)
    fancy_generator = async_numba_search(fibb(), make_predicate(3))
    try:
        print('OUTPUT: {}'.format(next(fancy_generator)))
        print('OUTPUT: {}'.format(next(fancy_generator)))
        # Interruption 1
        print('OUTPUT hi!')
        print('OUTPUT: {}'.format(next(fancy_generator)))
        print('OUTPUT: {}'.format(next(fancy_generator)))
        # Interruption 2
        print('OUTPUT: my name is bob!')
        print('OUTPUT: {}'.format(next(fancy_generator)))
        print('OUTPUT: {}'.format(next(fancy_generator)))
        print('OUTPUT: {}'.format(next(fancy_generator)))
        print('OUTPUT: {}'.format(next(fancy_generator)))
        print('OUTPUT: {}'.format(next(fancy_generator)))
        print('OUTPUT: {}'.format(next(fancy_generator)))
        print('OUTPUT: {}'.format(next(fancy_generator)))
        print('OUTPUT: {}'.format(next(fancy_generator)))
        # Interruption 3
        print('IF YOU SEE THIS SOMETHING IS WRONG')
    # HERE B MAGIC:
    except StopIteration as stopped:
        print("search completed with result: {!r}".format(stopped.value))
        print(hash_line)
    except Exception as some_exception:
        print('search failed with exception: {}'.format(some_exception))
        print(hash_line)


__MODULE_OUTPUT = """
        ################################################################
        testing our infinite-recursive sequence generator func.
        islice says "give me 20 vals from the generator."
        ================================================================
        OUTPUT: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
        ################################################################
        
        
        ################################################################
        make_predicate should always produce a conditional check-function
        in this case, it is looking for a number with `n` "figures"
        ================================================================
        n == 3
        sequence == [1, 20, 300, 4000, 50000]
        ----------------------------------------------------------------
        is_there_a_number_longer_than_n_digits = make_predicate(n)
        is_there_a_number_longer_than_n_digits(sequence)
        OUTPUT: True
        ################################################################
        
        
        ################################################################
        Testing our normal search function.
        your return statement will stop the function.
        ================================================================
        blocking_numba_search(fibb(), make_predicate(3))
        OUTPUT: 144
        ################################################################
        
        
        ################################################################
        A blocking-function can be turned into an async function by
        adding yield inside the iteration.
        ----------------------------------------------------------------
        Note that I can inject arbitrary jobs as I continue to call next.
        This is the behavior exploited to do ALL async things.
        ================================================================
        OUTPUT: Searching...
        OUTPUT: Searching...
        OUTPUT: hi!
        OUTPUT: Searching...
        OUTPUT: Searching...
        OUTPUT: my name is bob!
        OUTPUT: Searching...
        OUTPUT: Searching...
        OUTPUT: Searching...
        OUTPUT: Searching...
        OUTPUT: Searching...
        OUTPUT: Searching...
        OUTPUT: Searching...
        search completed with result: 144
        ################################################################
"""