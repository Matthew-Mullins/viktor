from .Constants import *
from .AccountDto import AccountDto
from .ActiveShardDto import ActiveShardDto
from .ChampionMasteryDto import ChampionMasteryDto
from .ChampionInfo import ChampionInfo
from .SummonerDto import SummonerDto

import requests

class Viktor():
    def __init__(self, api_key):
        self.api_key = api_key

    def QueryAPI(self, url):
        print(url)
        r = requests.get(url, headers={"X-Riot-Token": self.api_key})
        return r.json()

# ACCOUNT
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

# CHAMPION MASTERY
    def GetLOLChampionMasteriesBySummonerID(self, summonerID, region):
        champion_master_constant = CONSTANTS['champion-mastery']
        version = champion_master_constant['version']
        url_ext = champion_master_constant['urls']['champion-masteries-by-summoner-id'].format(version=version, encryptedSummonerId=summonerID)
        url = BASE_URL.format(region=region) + url_ext
        result = self.QueryAPI(url)
        cm_dto_list = set()
        for champion_mastery_dto in result:
            cm_dto_list.add(ChampionMasteryDto(champion_mastery_dto))
        return cm_dto_list

    def GetLOLChampionMasteryBySummonerID(self, summonerID, championID, region):
        champion_master_constant = CONSTANTS['champion-mastery']
        version = champion_master_constant['version']
        url_ext = champion_master_constant['urls']['champion-mastery-by-summoner-id-by-champion'].format(version=version, encryptedSummonerId=summonerID, championId=championID)
        url = BASE_URL.format(region=region) + url_ext
        return ChampionMasteryDto(self.QueryAPI(url))

    def GetLOLChampionMasteryScoreBySummonerID(self, summonerID, region):
        champion_master_constant = CONSTANTS['champion-mastery']
        version = champion_master_constant['version']
        url_ext = champion_master_constant['urls']['mastery-score-by-summoner-id'].format(version=version, encryptedSummonerId=summonerID)
        url = BASE_URL.format(region=region) + url_ext
        return self.QueryAPI(url)

# CHAMPION
    def GetLOLChampionRotations(self, region):
        champion_rotations_constant = CONSTANTS['champion-rotations']
        version = champion_rotations_constant['version']
        url_ext = champion_rotations_constant['urls']['champion-rotations'].format(version=version)
        url = BASE_URL.format(region=region) + url_ext
        return ChampionInfo(self.QueryAPI(url))

# CLASH
    def GetLOLClashPlayersBySummonerID(self, summonerId, region):
        pass

    def GetLOLClashTeamByTeamID(self, teamId, region):
        pass

    def GetLOLClashTournaments(self, region):
        pass

    def GetLOLClashTournamentByTeamID(self, teamId, region):
        pass

    def GetLOLClashTournamentByTournamentID(self, tournamentId, region):
        pass

# LEAGUE EXP
    def GetLOLEXPLeagueEntries(self, queue, tier, division, region):
        pass

# LEAGUE
    def GetLOLChallengerLeagueByQueue(self, queue, region):
        pass

    def GetLOLLeaguesBySummonerID(self, summonerId, region):
        pass

    def GetLOLLeagueEntries(self, queue, tier, division):
        pass

    def GetLOLGrandmasterLeagueByQueue(self, queue, region):
        pass

    def GetLOLLeagueByLeagueID(self, leagueId, region):
        pass

    def GetLOLMasterLeagueByQueue(self, queue, region):
        pass

# LOL STATUS
    def GetLOLStatus(self, region):
        pass

# LOR MATCH
    def GetLORMatchesByPUUID(self, puuid, region):
        pass

    def GetLORMatch(self, matchId, region):
        pass

# LOR RANKED
    def GetLORMasterTier(self, region):
        pass

# LOR STATUS
    def GetLORStatus(self, region):
        pass

# MATCH
    def GetLOLMatch(self, matchId, region):
        pass

    def GetLOLMatchlistFiltered(self, accountId, **kwargs):
        pass

    def GetLOLMatchTimeline(self, matchId, region):
        pass

    def GetLOLMatchesByTournamentCode(self, tournamentCode, region):
        pass

    def GetLOLMatchByTournamentCode(self, matchId, tournamentCode, region):
        pass

# SPECTATOR
    def GetLOLGameInfo(self, summonerId, region):
        pass

    def GetLOLFeaturedGames(self, region):
        pass

# SUMMONER
    def GetLOLSummonerByAccountID(self, accountId, region):
        pass
    
    def GetLOLSummonerBySummonerName(self, summonerName, region):
        summoner_constant = CONSTANTS['summoner']
        version = summoner_constant['version']
        url_ext = summoner_constant['urls']['summoner-by-name'].format(version=version, summonerName=summonerName)
        url = BASE_URL.format(region=region) + url_ext
        summoner = SummonerDto(self.QueryAPI(url))
        return summoner

    def GetLOLSummonerByPUUID(self, puuid, region):
        pass

    def GetLOLSummonerBySummonerID(self, summonerId, region):
        pass

# TFT LEAGUE
    def GetTFTChallenger(self, region):
        pass

    def GetTFTLeaguesBySummonerID(self, summonerId, region):
        pass

    def GetTFTLeague(self, tier, division, region):
        pass

    def GetTFTGrandmaster(self, region):
        pass

    def GetTFTLeagueByID(self, leagueId, region):
        pass

    def GetTFTMaster(self, region):
        pass

# TFT MATCH
    def GetTFTMatchIDsByPUUID(self, puuid, region):
        pass

    def GetTFTMatchByID(self, matchId, region):
        pass

# TFT SUMMONER
    def GetTFTSummonerByAccountID(self, accountId, region):
        pass

    def GetTFTSummonerBySummonerName(self, summonerName, region):
        pass

    def GetTFTSummonerByPUUID(self, puuid, region):
        pass

    def GetTFTSummonerBySummonerID(self, summonerId, region):
        pass

# THIRD PARTY CODE
    def GetThirdPartyCodeBySummonerID(self, summonerId, region):
        pass

# TOURNAMENT STUB

# TOURNAMENT

# VAL CONTENT
    def GetVALContentByLocale(self, region, **kwargs):
        pass

# VAL MATCH
    def GetVALMatchByID(self, matchId, region):
        pass

    def GetVALMatchlistByPUUID(self, puuid, region):
        pass

    def GetVALRecentMatchesByQueue(self, queue, region):
        pass

# VAL STATUS
    def GetVALStatus(self, region):
        pass
