# Another quote:
>## *"`asyncio` is friggin' dope b/c it bypasses the GIL entirely...*<br> *...just trust me. I'm a Philosopher."*
>~***Herodotus, BC 666***


<br>

## Step 1 --- Prepare to be mildly excited.

If you 
 
 
## Step 2 --- Clone the repo if you haven't already:
```shell
~$ git clone https://github.com/rtruxal/async_examples.git
~$ cd ./async_examples/comparisons/
```
*Double check cuz safety:*
```shell
~$ pwd
/path/to/cloned/repo/async_examples/comparisons
~$ ls
__init__.py  grampas_code.py  grandsons_code.py  
```
*Ok things look good. Let's begin:*
```shell
~$ python3 ./grampas_code.py
RUNNING MODULE: grandpas_code.py...

Grandpa doesn't know anything about asynchronous execution. 

Here's the output of his function:
xXxXxXxXxXxXxXxXxXxXx
xXxXxXxXxXxXxXxXxXxXx
xXxXxXxXxXxXxXxXxXxXx
xXxXxXxXxXxXxXxXxXxXx
xXxXxXxXxXxXxXxXxXxXx
xXxXxXxXxXxXxXxXxXxXx
xXxXxXxXxXxXxXxXxXxXx
xXxXxXxXxXxXxXxXxXxXx
xXxXxXxXxXxXxXxXxXxXx
xXxXxXxXxXxXxXxXxXxXx
xXxXxXxXxXxXxXxXxXxXx
I LOVE
I LOVE
I LOVE
I LOVE
I LOVE
I LOVE
I LOVE
I LOVE
I LOVE
I LOVE
I LOVE
EXPLOSIONS!
EXPLOSIONS!
EXPLOSIONS!
EXPLOSIONS!
EXPLOSIONS!
EXPLOSIONS!
EXPLOSIONS!
EXPLOSIONS!
EXPLOSIONS!
EXPLOSIONS!
EXPLOSIONS!

Begun: Wed Aug  2 13:50:29 2017
Ended: Wed Aug  2 13:50:59 2017
DURATION: 30.01106548309326 seconds
```
```shell
~$ python3 grandsons_code.py
RUNNING MODULE: grandsons_code.py

Grandson is a follower of the philosopher Herodotus & has mastered asynchronous execution.

Here's the output of his function:
xXxXxXxXxXxXxXxXxXxXx
I LOVE
EXPLOSIONS!
xXxXxXxXxXxXxXxXxXxXx
I LOVE
xXxXxXxXxXxXxXxXxXxXx
EXPLOSIONS!
xXxXxXxXxXxXxXxXxXxXx
I LOVE
xXxXxXxXxXxXxXxXxXxXx
xXxXxXxXxXxXxXxXxXxXx
I LOVE
EXPLOSIONS!
xXxXxXxXxXxXxXxXxXxXx
xXxXxXxXxXxXxXxXxXxXx
I LOVE
xXxXxXxXxXxXxXxXxXxXx
EXPLOSIONS!
xXxXxXxXxXxXxXxXxXxXx
I LOVE
xXxXxXxXxXxXxXxXxXxXx
EXPLOSIONS!
I LOVE
I LOVE
EXPLOSIONS!
I LOVE
EXPLOSIONS!
I LOVE
I LOVE
EXPLOSIONS!
EXPLOSIONS!
EXPLOSIONS!
EXPLOSIONS!

Begun: Wed Aug  2 13:57:49 2017
Ended: Wed Aug  2 13:58:04 2017
DURATION: 15.024974584579468 seconds
```