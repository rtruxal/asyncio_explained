# stolen from: https://7webpages.com/blog/writing-online-multiplayer-game-with-python-and-asyncio-writing-game-loop/
# import async_timeout
# import aiohttp

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
from aiohttp import web
import aiofiles


SERVER_ADDR = ('', 8808)


async def ticker_loop(app):
    """
    This func does 2 things:
     - it turns the service on/off depending on whether there are open connections.
     - it sends a tick to each connected client every 2 seconds

    :param app: dictionary-like object used to share info b/w clients.
    :return: None
    """
    # First time this gets called is when a "client"/input-thread connects.
    app["service_running"] = True
    # keepalive beacon every 2 seconds.
    while True:
        # Rather than getting fancy w/ switching logic, I'm just changing 2 iterations into 1.

        # iter 1
        for websock in app['sockets']:
            websock.send_str("tick")
        if len(app['sockets']) == 0:
            break
        await asyncio.sleep(2)
        # iter 2
        for websock in app["sockets"]:
            websock.send_str("tock")
        if len(app["sockets"]) == 0:
            break
        await asyncio.sleep(2)

    app["service_running"] = False


async def handle_websock(request):
    # BOOKKEEPING:
    # ...at some point `app` must get set as an attr of `request`.
    app = request.app
    websock = web.WebSocketResponse()
    # pass the baton back to the loop until `prepare()` is ready.
    await websock.prepare(request)
    app["sockets"].append(websock)
    #TODO: Why did we change this location? What is ensure_future() really doing?
    if app["service_running"] == False:
        asyncio.ensure_future(ticker_loop(app))
    # LOGIC:
    while True:
        # If possible, try to put an await at the top of a block.
        # This allows you to write loop-iterations in a way that is easy to read.
        msg = await websock.receive()
        if msg.tp == web.MsgType.text:
            print('got "{}" from the client.'.format(msg.data))
            websock.send_str('You entered: "{}".'.format(msg.data))
        elif msg.tp == web.MsgType.error or msg.tp == web.MsgType.close:
            break
    app["sockets"].remove(websock)
    print("Closed a connection.")
    return websock

async def handle_webpage(request):
    # the original sourcecode opens the html without context-management
    # I learned about the `aiofiles` package because of this:
    async with aiofiles.open('index.html', 'rb') as index:
        # note the `await`. Without it, we get back a generator.
        content = await index.read()
    return web.Response(body=content, content_type='text/html')



if __name__ == '__main__':
    try:
        from uvloop import EventLoopPolicy
        asyncio.set_event_loop_policy(EventLoopPolicy())
    except ImportError:
        print('INFO: uvloop asyncio-accelerator for UNIX is not installed.')
        pass

    app = web.Application()
    app['sockets'] = []
    app["service_running"] = False

    #TODO: Why did we move `ensure_future()` from here to `handle_websock()`?
    # asyncio.ensure_future(ticker_loop(app))

    app.router.add_route('GET', '/connect', handle_websock)
    app.router.add_route('GET', '/', handle_webpage)
    try:
        web.run_app(app, port=SERVER_ADDR[1])
    except KeyboardInterrupt:
        web.raise_graceful_exit()
