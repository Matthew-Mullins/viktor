class ChampionInfo():
    def __init__(self, championInfo):
        self.maxNewPlayerLevel = championInfo.get('maxNewPlayerLevel')
        self.freeChampionIdsForNewPlayers = championInfo.get('freeChampionIdsForNewPlayers')
        self.freeChampionIds = championInfo.get('freeChampionIds')

    def __repr__(self):
        return  'Max New Player Level: {maxNewPlayerLevel}\n'\
                'Free Champion IDs for New Players: {freeChampionIdsForNewPlayers}\n'\
                'Free Champion IDs: {freeChampionIds}'.format(
                    maxNewPlayerLevel = self.maxNewPlayerLevel,
                    freeChampionIdsForNewPlayers = self.freeChampionIdsForNewPlayers,
                    freeChampionIds = self.freeChampionIds
                )