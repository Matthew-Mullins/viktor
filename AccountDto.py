from .Constants import CONSTANTS

import json
import requests

class AccountDto():
    def __init__(self, puuid, gameName=None, tagLine=None):
        self.puuid = puuid
        self.gameName = gameName
        self.tagLine = tagLine

    @classmethod
    def GetAccountByPUUID(puuid):
        url = CONSTANTS['account']['urls']['account-by-puuid']

    @classmethod
    def GetAccountByRiotID(gameName, tagLine):
        pass