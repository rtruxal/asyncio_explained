import aiohttp
# import async_http
import asyncio
import async_timeout
import os


async def download_coroutine(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            filename = os.path.basename(url)
            with open(filename, 'wb') as file_handle:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    file_handle.write(chunk)
            return await response.release()


async def main(loop=None):
    if loop:
        urls = [
            "https://httpbin.org",
            "https://bing.com",
            "https://google.com",
            "http://please.buythingsfrom.us",
        ]
        async with aiohttp.ClientSession(loop=loop) as session:
            tasks = [download_coroutine(session, url) for url in urls]
            await asyncio.gather(*tasks)
    else:
        exit(1)



if __name__ == '__main__':
    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except ImportError:
        pass

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))