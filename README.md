# async_explained

## Ramble:

Hey! You know how the `asyncio` python module ***makes absolutely no sense at best & made me break my laptop at worst/that actually happened?,*** but that it is also somehow extremely important & **""""BEST practice"""""** .  

#### ***Question:*** 
As a respectable f\*Xing professional, how can I convince myself to learn this?  

#### ***Answer:*** 
> #### *"Don't be a pussy. You got this. Now follow the instructions & stop it."*
>~***Herodotus, BC 436***



## The Paradigm-Shift:
The 10,000ft difference between typical python programs `asyncio`-based programs **involves shifting the responsibility of determining execution-flow.**  
  - **They shift it from:**
    - `main()`, or some other single function which runs top-to-bottom, calling other funcs when necessary.  
  - **to:**
    - many async/non-blocking functions, wherein a `yield` can be thought of as pressing a "submit button." 
      
#### Programs obeying the asyncio paraigm DO NOT run top-to-bottom.  
#### The `asyncio` design-pattern means executing code ***in the order that non-blocking functions MASH on the "submit button" (aka perform a yield.)*** 
      

<br><br>


## How to Use This Package:
Run each module independently to see the results produced. `async_basics.py` in particular has formatted output to make the code easier to understand.

1. **BEGIN by running** `comparisons/grandpas_code.py` & `comparisons/grandsons_code.py` side-by-side **AND STAND IN AWE OF THE POWER of asynchronous process execution.** \*\**sound-of-lightning-in-the-distance*\*\* 

2. **Run & then read** `async_basics.py` to get the fundamentals down.**  

3. **Run & then read** `emulating_async_classes_with_stdlib.py` to see how some of the `asyncio` classes work.**  

4. **Run & then read** `yield_and_yield_from.py` to learn how the previous two modules get abbreviated by using the `asyncio` syntax provided to us by the people who made me switch to python3.**  

<br><br>
# RE:
>*"I hate reading code. Please use mouth-words."*  
~***Herodotus, BC 444***


- **`asyncio` loops create coroutines by exploiting the following behavior of NON-BLOCKING functions:**
  - they are state-saving.
  - they produce callable objects.        
- **What is a NON-BLOCKING function?**
  - GENERATOR functions contain a yield statement & need to be fXXing hand-held through execution.
  - BLOCKING functions contain a return statement. They'll get in your way, they dont give AF.
  - **NON-BLOCKING** functions contain BOTH a `yield` AND `return` statement. They're dope. Just ask Jeremy.  
    - non-blocking functions MUST ALWAYS call `yield` at least 1 time.
- **How do these loops do this?**
  - With something called a Scheduler. 
    - It's basically a fancy queue.
  - This topic is covered in `emulating_async_classes_with_stdlib.py`

- **Why do I need to monkeypatch so friggin' much?**
  - Clearly you already know a bit about this.
  - That topic is covered in `yield_and_yield_from.py`