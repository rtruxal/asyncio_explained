# async_explained

### How to use this package:
Run each module independently to see the results produced. `async_basics.py` in particular has formatted output to make the code easier to understand.


1. **Run & then read `async_basics.py` to get the fundamentals down.**  

2. **Run & then read `emulating_async_classes_with_stdlib.py` to see how some of the `asyncio` classes work.**  

3. **Run & then read `yield_and_yield_from.py` to learn how the previous implementations are used with the `asyncio` syntax context.**  

  
  
### Fundamental concepts:
- **`asyncio` loops create coroutines by exploiting the following behavior of NON-BLOCKING functions.**
  - they are state-saving.
    - they produce callable objects.        
- **What is a NON-BLOCKING function?**
  - GENERATOR functions contain a yield statement.
  - BLOCKING functions contain a return statement.
  - **NON-BLOCKING** functions contain BOTH a yield AND return statement.
          - non-blocking functions MUST ALWAYS call yield at least 1 time.
- **How do these loops do this?**
  - With something called a Scheduler. 
    - It's basically a fancy queue.
  - This topic is covered in `emulating_async_classes_with_stdlib.py`

- **Why do I need to monkeypatch so friggin' much?**
  - Clearly you already know a bit about this.
  - This topic is covered in `yield_and_yield_from.py`