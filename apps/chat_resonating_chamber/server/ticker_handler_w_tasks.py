#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
from aiohttp import web
import aiofiles

#TODO: Rob you need to learn JavaScript.
async def handle_webpage(request):
    async with aiofiles.open('index.html', 'rb') as index:
        content = await index.read()
    return web.Response(body=content, content_type='text/html')



async def handle_websock(request):
    # BOOKKEEPING
    app = request.app
    websock = web.WebSocketResponse()
    await websock.prepare(request)
    # TASK-MANAGEMENT
    if app["service_loop"] is None or app["service_loop"].cancelled():
        app["service_loop"] = asyncio.ensure_future(ticker(app))
        # Otherwise this will fail silently...gotta love asyncio.
        app["service_loop"].add_done_callback(lambda t: t.result() if not t.cancelled() else None)
    # LOGIC
    # not putting intro method here. ticker starts when someone joins. Adding there.
    app["sockets"].append(websock)
    while True:
        msg = await websock.receive()
        if msg.tp == web.MsgType.text:
            websock.send_str("Pressed key having code: {}".format(msg.data))
            print("got code {} from a client.".format(msg.data))
        # looool there's `.close`, `.closed`, & `.closing`. (>_<)
        elif msg.tp == web.MsgType.error or\
            msg.tp == web.MsgType.close:
            break
    app["sockets"].remove(websock)
    # CLOSING
    if len(app["sockets"]) == 0:
        print('0 CONNECTIONS. SUSPENDING LOOP.')
        app["service_loop"].cancel()
    print("Closed Connection.")

    return websock


async def ticker(app):
    print("INITIAL CONNECTION ESTABLISHED. SERVICE LOOP STARTING.")
    while True:
        for ws in app["sockets"]:
            ws.send_str("PING!")
        await asyncio.sleep(4)



if __name__ == '__main__':
    app = web.Application()

    app["service_loop"] = None
    app["sockets"] = []

    app.router.add_route('GET', '/', handle_webpage)
    app.router.add_route('GET', '/connect', handle_websock)

    web.run_app(app)