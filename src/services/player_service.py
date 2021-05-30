

from models.snake_ladder_player import Player
from helper import id_generator


class PlayerService:
    
    @staticmethod
    def create_players(players,noOfPlayers):
        for player in range(1,noOfPlayers):
            players.append(Player(id_generator()))
        return players