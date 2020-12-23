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
            'summoner-by-account-id': '/lol/summoner/{version}/summoners/by-account/{encryptedAccountId}',
            'summoner-by-summoner-name': '/lol/summoner/{version}/summoners/by-name/{summonerName}',
            'summoner-by-puuid': '/lol/summoner/{version}/summoners/by-puuid/{encryptedPUUID}',
            'summoner-by-summoner-id': '/lol/summoner/{version}/summoners/{encryptedSummonerId}'
        }
    },
    'tft-league': {
        'version': 'v1',
        'game': 'Teamfight Tactics',
        'urls': {
            'challenger-league': '/tft/league/{version}/challenger',
            'leagues-by-summoner-id': '/tft/league/{version}/entries/by-summoner/{encryptedSummonerId}',
            'league-entries': '/tft/league/{version}/entries/{tier}/{division}',
            'grandmaster-league': '/tft/league/{version}/grandmaster',
            'league-by-id': '/tft/league/{version}/leagues/{leagueId}',
            'master-league': '/tft/league/{version}/master'
        }
    },
    'tft-match': {
        'version': 'v1',
        'game': 'Teamfight Tactics',
        'urls': {
            'matches-by-puuid': '/tft/match/{version}/matches/by-puuid/{puuid}/ids',
            'match-by-match-id': '/tft/match/{version}/matches/{matchId}'
        }
    },
    'tft-summoner': {
        'version': 'v1',
        'game': 'Teamfight Tactics',
        'urls': {
            'summoner-by-account-id': '/tft/summoner/{version}/summoners/by-account/{encryptedAccountId}',
            'summoner-by-summoner-name': '/tft/summoner/{version}/summoners/by-name/{summonerName}',
            'summoner-by-puuid': '/tft/summoner/{version}/summoners/by-puuid/{encryptedPUUID}',
            'summoner-by-summonerid': '/tft/summoner/{version}/summoners/{encryptedSummonerId}'
        }
    },
    'third-party-code': {
        'version': 'v4',
        'game': 'League of Legends',
        'urls': {
            'by-summoner-id': '/lol/platform/{version}/third-party-code/by-summoner/{encryptedSummonerId}'
        }
    },
    'tournament-stub': {
        'version': 'v4',
        'game': 'League of Legends',
        'urls': {
            'create-tournament-code': '/lol/tournament-stub/{version}/codes',
            'lobby-events-by-code': '/lol/tournament-stub/{version}/lobby-events/by-code/{tournamentCode}',
            'create-tournament-provider': '/lol/tournament-stub/{version}/providers',
            'create-tournament': '/lol/tournament-stub/{version}/tournaments'
        }
    },
    'tournament': {
        'version': 'v4',
        'game': 'League of Legends',
        'urls': {
            'create-tournament-code': '/lol/tournament/{version}/codes',
            'tournament-dto-by-code': '/lol/tournament/{version}/codes/{tournamentCode}',
            'update-tournament-by-code': '/lol/tournament/{version}/codes/{tournamentCode}',
            'lobby-events-by-code': '/lol/tournament/{version}/lobby-events/by-code/{tournamentCode}',
            'create-tournament-provider': '/lol/tournament/{version}/providers',
            'create-tournament': '/lol/tournament/{version}/tournaments'
        }
    },
    'val-content': {
        'version': 'v1',
        'game': 'Valorant',
        'urls': {
            'content-by-locale': '/val/content/{version}/contents'
        }
    },
    'val-match': {
        'version': 'v1',
        'game': 'Valorant',
        'urls': {
            'match-by-id': '/val/match/{version}/matches/{matchId}',
            'matchlist-by-puuid': '/val/match/{version}/matchlists/by-puuid/{puuid}',
            'recent-matches-by-queue': '/val/match/{version}/recent-matches/by-queue/{queue}'
        }
    },
    'val-status': {
        'version': 'v1',
        'game': 'Valorant',
        'urls': {
            'status': '/val/status/v1/platform-data'
        }
    }
}