from .Constants import *
from .AccountDto import AccountDto
from .ActiveShardDto import ActiveShardDto
from .SummonerDto import SummonerDto

import requests

class Viktor():
    def __init__(self, api_key):
        self.api_key = api_key

    def QueryAPI(self, url):
        print(url)
        r = requests.get(url, headers={"X-Riot-Token": self.api_key})
        return r.json()

    def GetAccountByPUUID(self, puuid, region):
        account_constant = CONSTANTS['account']
        version = account_constant['version']
        url_ext = account_constant['urls']['account-by-puuid'].format(version=version, puuid=puuid)
        url = BASE_URL.format(region=region) + url_ext
        account = AccountDto(self.QueryAPI(url))
        return account

    def GetAccountByRiotID(self, gameName, tagLine, region):
        account_constant = CONSTANTS['account']
        version = account_constant['version']
        url_ext = account_constant['urls']['account-by-riot-id'].format(version=version, gameName=gameName, tagLine=tagLine)
        url = BASE_URL.format(region=region) + url_ext
        account = AccountDto(self.QueryAPI(url))
        return account

    def GetActiveShardByPUUID(self, game, puuid, region):
        account_constant = CONSTANTS['account']
        version = account_constant['version']
        url_ext = account_constant['urls']['active-shard-by-game-by-puuid'].format(version=version, game=game, puuid=puuid)
        url = BASE_URL.format(region=region) + url_ext
        active_shard = ActiveShardDto(self.QueryAPI(url))
        return active_shard

    def GetSummonerBySummonerName(self, summonerName, region):
        summoner_constant = CONSTANTS['summoner']
        version = summoner_constant['version']
        url_ext = summoner_constant['urls']['summoner-by-name'].format(version=version, summonerName=summonerName)
        url = BASE_URL.format(region=region) + url_ext
        summoner = SummonerDto(self.QueryAPI(url))
        return summoner