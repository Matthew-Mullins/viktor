import json
import requests

def GetAccountByPUUID(puuid):
    pass

def GetAccountByRiotID(gameName, tagLine):
    pass

class Account():
    def __init__(self, puuid, gameName=None, tagLine=None):
        self.puuid = puuid
        self.gameName = gameName
        self.tagLine = tagLine