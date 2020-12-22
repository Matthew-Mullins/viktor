from .Constants import *
from .AccountDto import AccountDto
from .ActiveShardDto import ActiveShardDto
from .ChampionMasteryDto import ChampionMasteryDto
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

    def GetChampionMasteriesBySummonerID(self, summonerID, region):
        champion_master_constant = CONSTANTS['champion-mastery']
        version = champion_master_constant['version']
        url_ext = champion_master_constant['urls']['champion-masteries-by-summoner-id'].format(version=version, encryptedSummonerId=summonerID)
        url = BASE_URL.format(region=region) + url_ext
        result = self.QueryAPI(url)
        cm_dto_list = set()
        for champion_mastery_dto in result:
            cm_dto_list.add(ChampionMasteryDto(champion_mastery_dto))
        return cm_dto_list

    def GetChampionMasteryBySummonerID(self, summonerID, championID, region):
        champion_master_constant = CONSTANTS['champion-mastery']
        version = champion_master_constant['version']
        url_ext = champion_master_constant['urls']['champion-mastery-by-summoner-id-by-champion'].format(version=version, encryptedSummonerId=summonerID, championId=championID)
        url = BASE_URL.format(region=region) + url_ext
        return ChampionMasteryDto(self.QueryAPI(url))

    def GetChampionMasteryScoreBySummonerID(self, summonerID, region):
        champion_master_constant = CONSTANTS['champion-mastery']
        version = champion_master_constant['version']
        url_ext = champion_master_constant['urls']['mastery-score-by-summoner-id'].format(version=version, encryptedSummonerId=summonerID)
        url = BASE_URL.format(region=region) + url_ext
        return self.QueryAPI(url)

    def GetSummonerBySummonerName(self, summonerName, region):
        summoner_constant = CONSTANTS['summoner']
        version = summoner_constant['version']
        url_ext = summoner_constant['urls']['summoner-by-name'].format(version=version, summonerName=summonerName)
        url = BASE_URL.format(region=region) + url_ext
        summoner = SummonerDto(self.QueryAPI(url))
        return summoner