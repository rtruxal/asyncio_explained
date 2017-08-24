import asyncio
import sys
import os


class Resonator(object):
    def __init__(self, name="default", loop=None):
        # name, empty mapping dictionary, & if a specific loop is provided, use it.
        self._name = name
        self._transports = {}
        if not loop:
            self._loop = asyncio.get_event_loop()
        else:
            self._loop = loop


class Protocol(asyncio.Protocol):
    def __init__(self, resonator_name):
        self._resonator_name = resonator_name
        self._connection_identifier = None
        self._transport = None
        self._buffer = []

    def connection_made(self, transport):
        self._transport = transport
        self._writeline()

    # shorthand transport writing methods
    def _write(self, text):
        self._transport.write(text.encode('utf-8'))

    def _writeline(self, line):
        self._write(line)
        self._write(os.linesep)