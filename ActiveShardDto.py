class ActiveShardDto():
    def __init__(self, activeShardDto):
        self.puuid = activeShardDto.get('puuid')
        self.game = activeShardDto.get('game')
        self.activeShard = activeShardDto.get('activeShard')

    def __repr__(self):
        return  'Game: {game}\n'\
                'PUUID: {puuid}\n'\
                'Active Shard: {activeShard}'.format(
                    game=self.game,
                    puuid=self.puuid,
                    activeShard=self.activeShard
                )