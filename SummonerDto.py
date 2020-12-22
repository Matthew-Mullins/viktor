class SummonerDto():
    def __init__(self, summonerDto):
        self.id = summonerDto.get('id')
        self.account_id = summonerDto.get('accountId')
        self.puuid = summonerDto.get('puuid')
        self.name = summonerDto.get('name')
        self.profileIconId = summonerDto.get('profileIconId')
        self.revisionDate = summonerDto.get('revisionDate')
        self.summonerLevel = summonerDto.get('summonerLevel')

    def __repr__(self):
        return  'Summoner Name: {summonerName}\n'\
                'Summoner Level: {summonerLevel}\n'\
                'Summoner ID: {summonerID}\n'\
                'Account ID: {accountID}\n'\
                'PUUID: {puuid}'.format(
                    summonerName=self.name,
                    summonerLevel=self.summonerLevel,
                    summonerID=self.id,
                    accountID=self.account_id,
                    puuid=self.puuid
                )