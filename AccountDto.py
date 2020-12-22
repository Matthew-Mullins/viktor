class AccountDto():
    def __init__(self, accountDto):
        self.puuid = accountDto.get('puuid')
        self.gameName = accountDto.get('gameName', 'Game Name Does Not Exist')
        self.tagLine = accountDto.get('tagLine', 'Tag Line Does Not Exist')

    def __repr__(self):
        return  'Game Name: {gameName}\n'\
                'Tag Line: {tagLine}\n'\
                'PUUID: {puuid}'.format(
                    gameName=self.gameName,
                    tagLine=self.tagLine,
                    puuid=self.puuid
                )