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

    def QueryAPI(self, api_name, api_ext_name, region, **kwargs):
        api_constant = CONSTANTS[api_name]
        version = api_constant['version']
        url_ext = api_constant['urls'][api_ext_name].format(version=version, **kwargs)
        url = BASE_URL.format(region=region) + url_ext
        r = requests.get(url, headers={'X-Riot-Token': self.api_key})
        print(r.status_code)
        return r.json()

# ACCOUNT
    def GetAccountByPUUID(self, puuid, region):
        return AccountDto(self.QueryAPI('account', 'account-by-puuid', region, puuid=puuid))

    def GetAccountByRiotID(self, gameName, tagLine, region):
        return AccountDto(self.QueryAPI('account', 'account-by-riot-id', region, gameName=gameName, tagLine=tagLine))

    def GetActiveShardByPUUID(self, game, puuid, region):
        return ActiveShardDto(self.QueryAPI('account', 'active-shard-by-game-by-puuid', region, game=game, puuid=puuid))

# CHAMPION MASTERY
    def GetLOLChampionMasteriesBySummonerID(self, summonerId, region):
        cm_dto_list = set()
        r = self.QueryAPI('champion-mastery', 'champion-masteries-by-summoner-id', region, encryptedSummonerId=summonerId)
        for champion_mastery_dto in r:
            cm_dto_list.add(ChampionMasteryDto(champion_mastery_dto))
        return cm_dto_list

    def GetLOLChampionMasteryBySummonerID(self, summonerId, championId, region):
        return ChampionMasteryDto(self.QueryAPI('champion-mastery', 'champion-mastery-by-summoner-id-by-champion', region, encryptedSummonerId=summonerId, championId=championId))

    def GetLOLChampionMasteryScoreBySummonerID(self, summonerId, region):
        return self.QueryAPI('champion-mastery', 'mastery-score-by-summoner-id', region, encryptedSummonerId=summonerId)

# CHAMPION
    def GetLOLChampionRotations(self, region):
        return self.QueryAPI('champion-rotations', 'champion-rotations', region)

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
        return SummonerDto(self.QueryAPI('summoner', 'summoner-by-account-id', region, encryptedAccountId=accountId))
    
    def GetLOLSummonerBySummonerName(self, summonerName, region):
        return SummonerDto(self.QueryAPI('summoner', 'summoner-by-summoner-name', region, summonerName=summonerName))

    def GetLOLSummonerByPUUID(self, puuid, region):
        return SummonerDto(self.QueryAPI('summoner', 'summoner-by-puuid', region, puuid=puuid))

    def GetLOLSummonerBySummonerID(self, summonerId, region):
        return SummonerDto(self.QueryAPI('summoner', 'summoner-by-summoner-id', region, encryptedSummonerId=summonerId))

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
