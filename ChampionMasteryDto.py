class ChampionMasteryDto():
    def __init__(self, championMasteryDto):
        self.championPointsUntilNextLevel = championMasteryDto.get('championPointsUntilNextLevel')
        self.chestGranted = championMasteryDto.get('chestGranted')
        self.championId = championMasteryDto.get('championId')
        self.lastPlayTime = championMasteryDto.get('lastPlayTime')
        self.championLevel = championMasteryDto.get('championLevel')
        self.summonerId = championMasteryDto.get('summonerId')
        self.championPoints = championMasteryDto.get('championPoints')
        self.championPointsSinceLastLevel = championMasteryDto.get('championPointsSinceLastLevel')
        self.tokensEarned = championMasteryDto.get('tokensEarned')

    def __repr__(self):
        return  'Summoner ID: {summonerId}\n'\
                'Champion ID: {championId}\n'\
                'Champion Level: {championLevel}\n'\
                'Champion Points: {championPoints}\n'\
                'Champion Points Until Next Level: {championPointsUntilNextLevel}\n'\
                'Champion Points Since Last Level: {championPointsSinceLastLevel}\n'\
                'Tokens Earned: {tokensEarned}\n'\
                'Chest Granted: {chestGranted}\n'\
                'Last Play Time: {lastPlayTime}\n'.format(
                    summonerId = self.summonerId,
                    championId = self.championId,
                    championLevel = self.championLevel,
                    championPoints = self.championPoints,
                    championPointsUntilNextLevel = self.championPointsUntilNextLevel,
                    championPointsSinceLastLevel = self.championPointsSinceLastLevel,
                    tokensEarned = self.tokensEarned,
                    chestGranted = self.chestGranted,
                    lastPlayTime = self.lastPlayTime
                )