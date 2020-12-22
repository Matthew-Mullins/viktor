from .Viktor import Viktor
from .Constants import BASE_URL, CONSTANTS

import requests

def GetAccountBySummonerName(summonerName, region):
    summoner_constant = CONSTANTS['summoner']
    version = summoner_constant['version']
    url = summoner_constant['urls']['summoner-by-name'].format(version=version, summonerName=summonerName)
    r = requests.get(BASE_URL.format(region=region) + url, headers={"X-Riot-Token": Viktor.api_key})
    result = r.json()
    return result

class SummonerDto():
    def __init__(self, summonerDto):
        self.account_id = summonerDto['accountId']
        self.id = summonerDto['id']
        self.name = summonerDto['name']
        self.profileIconId = summonerDto['profileIconId']
        self.puuid = summonerDto['puuid']
        self.revisionDate = summonerDto[]