BASE_URL = 'https://{region}.api.riotgames.com'
CONSTANTS = {
    'account': {
        'version': 'v1',
        'game': 'Legends of Runeterra',
        'urls': {
            'account-by-puuid': '/riot/account/{version}/accounts/by-puuid/{puuid}',
            'account-by-riot-id': '/riot/account/{version}/accounts/by-riot-id/{gameName}/{tagLine}',
            'active-shard-by-game-by-puuid': '/riot/account/{version}/active-shards/by-game/{game}/by-puuid/{puuid}'
        }
    },
    'champion-mastery': {
        'version': 'v4',
        'game': 'League of Legends',
        'urls': {
            'champion-masteries-by-summoner-id': '/lol/champion-mastery/{version}/champion-masteries/by-summoner/{encryptedSummonerId}',
            'champion-mastery-by-summoner-id-by-champion': '/lol/champion-mastery/{version}/champion-masteries/by-summoner/{encryptedSummonerId}/by-champion/{championId}',
            'mastery-score-by-summoner-id': '/lol/champion-mastery/{version}/scores/by-summoner/{encryptedSummonerId}'
        }
    },
    'champion-rotations': {
        'version': 'v3',
        'game': 'League of Legends',
        'urls': {
            'champion-rotations': '/lol/platform/{version}/champion-rotations'
        }
    },
    'clash': {
        'version': 'v1',
        'game': 'League of Legends',
        'urls': {
            'players-by-summoner-id': '/lol/clash/{version}/players/by-summoner/{summonerId}',
            'team-by-id': '/lol/clash/{version}/teams/{teamId}',
            'tournaments': '/lol/clash/{version}/tournaments',
            'tournament-by-team-id': '/lol/clash/{version}/tournaments/by-team/{teamId}',
            'tournament-by-id': '/lol/clash/{version}/tournaments/{tournamentId}'
        }
    },
    'league-exp': {
        'version': 'v4',
        'game': 'League of Legends',
        'urls': {
            'league-entries': '/lol/league-exp/{version}/entries/{queue}/{tier}/{division}'
        }
    },
    'league': {
        'version': 'v4',
        'game': 'League of Legends',
        'urls': {
            'challenger-by-queue': '/lol/league/{version}/challengerleagues/by-queue/{queue}',
            'leagues-by-summoner-id': '/lol/league/{version}/entries/by-summoner/{encryptedSummonerId}',
            'league-entries': '/lol/league/{version}/entries/{queue}/{tier}/{division}',
            'grandmaster-by-queue': '/lol/league/{version}/grandmasterleagues/by-queue/{queue}',
            'league-by-id': '/lol/league/{version}/leagues/{leagueId}',
            'master-by-queue': '/lol/league/{version}/masterleagues/by-queue/{queue}'
        }
    },
    'lol-status': {
        'version': 'v4',
        'game': 'League of Legends',
        'urls': {
            'status': '/lol/status/{version}/platform-data'
        }
    },
    'lor-match': {
        'version': 'v1',
        'game': 'Legends of Runeterra',
        'urls': {
            'matches-by-puuid': '/lor/match/{version}/matches/by-puuid/{puuid}/ids',
            'match-by-match-id': '/lor/match/{version}/matches/{matchId}'
        }
    },
    'lor-ranked': {
        'version': 'v1',
        'game': 'Legends of Runeterra',
        'urls': {
            'players-in-master': '/lor/ranked/{version}/leaderboards'
        }
    },
    'lor-status': {
        'version': 'v1',
        'game': 'Legends of Runeterra',
        'urls': {
            'status': '/lor/status/{version}/platform-data'
        }
    },
    'match': {
        'version': 'v4',
        'game': 'League of Legends',
        'urls': {
            'match-ids-by-tournament-code': '/lol/match/{version}/matches/by-tournament-code/{tournamentCode}/ids',
            'match-by-id': '/lol/match/{version}/matches/{matchId}',
            'match-by-id-by-tournament-code': '/lol/match/{version}/matches/{matchId}/by-tournament-code/{tournamentCode}',
            'matchlist-filtered': '/lol/match/{version}/matchlists/by-account/{encryptedAccountId}',
            'timeline-by-match-id': '/lol/match/{version}/timelines/by-match/{matchId}'
        }
    },
    'spectator': {
        'version': 'v4',
        'game': 'League of Legends',
        'urls': {
            'current-game-by-summoner-id': '/lol/spectator/{version}}/active-games/by-summoner/{encryptedSummonerId}',
            'featured-games': '/lol/spectator/{version}/featured-games'
        }
    },
    'summoner': {
        'version': 'v4',
        'game': 'League of Legends',
        'urls': {
            'summoner-by-name': '/lol/summoner/{version}/summoners/by-name/{summonerName}'
        }
    },
    'tft-league': {
        'version': '',
        'game': '',
        'urls': {
            
        }
    },
    'tft-match': {
        'version': '',
        'game': '',
        'urls': {
            
        }
    },
    'tft-summoner': {
        'version': '',
        'game': '',
        'urls': {
            
        }
    },
    'third-party-code': {
        'version': '',
        'game': '',
        'urls': {
            
        }
    },
    'tournament-stub': {
        'version': '',
        'game': '',
        'urls': {
            
        }
    },
    'tournament': {
        'version': '',
        'game': '',
        'urls': {
            
        }
    },
    'val-content': {
        'version': '',
        'game': '',
        'urls': {
            
        }
    },
    'val-match': {
        'version': '',
        'game': '',
        'urls': {
            
        }
    },
    'val-status': {
        'version': '',
        'game': '',
        'urls': {
            
        }
    }
}