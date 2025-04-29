import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            str(config.STRING1),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.two = Client(
            str(config.STRING2),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.three = Client(
            str(config.STRING3),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.four = Client(
            str(config.STRING4),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )
        self.five = Client(
            str(config.STRING5),
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            no_updates=True,
        )