# async_explained

## Ramble:

Hey! You know how the `asyncio` python module ***makes absolutely no sense at best & made me break my laptop at worst/that actually happened?,*** but that it is also somehow extremely important & **""""BEST practice"""""** .  

#### ***Question:*** 
As a respectable f\*Xing professional, how can I convince myself to learn this?  

#### ***Answer:*** 
> #### *"Don't be a pussy. You got this. Now follow the instructions & stop it."*
>~***Herodotus, BC 436***


<br><br>


## How to use this package:
Run each module independently to see the results produced. `async_basics.py` in particular has formatted output to make the code easier to understand.


1. **Run & then read `async_basics.py` to get the fundamentals down.**  

2. **Run & then read `emulating_async_classes_with_stdlib.py` to see how some of the `asyncio` classes work.**  

3. **Run & then read `yield_and_yield_from.py` to learn how the previous two modules get abbreviated by using the `asyncio` syntax provided to us by the people who made me switch to python3.**  

<br><br>
# RE:
>*"I hate reading code. Please use mouth-words."*  
~***Herodotus, BC 444***
<br><br>
- **`asyncio` loops create coroutines by exploiting the following behavior of NON-BLOCKING functions.**
  - they are state-saving.
  - they produce callable objects.        
- **What is a NON-BLOCKING function?**
  - GENERATOR functions contain a yield statement & need to be fXXing hand-held through execution.
  - BLOCKING functions contain a return statement. They'll get in your way, they dont give AF.
  - **NON-BLOCKING** functions contain BOTH a yield AND return statement. They're dope. Just ask Jeremy.  
    - non-blocking functions MUST ALWAYS call yield at least 1 time.
- **How do these loops do this?**
  - With something called a Scheduler. 
    - It's basically a fancy queue.
  - This topic is covered in `emulating_async_classes_with_stdlib.py`

- **Why do I need to monkeypatch so friggin' much?**
  - Clearly you already know a bit about this.
  - That topic is covered in `yield_and_yield_from.py`