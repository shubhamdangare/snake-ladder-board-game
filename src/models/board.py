


class SnakeAndLadderBoard():
    
    def __init__(self, size):
        self.size = size
        self.snakes = list()
        self.ladders = list()
        self.player_pieces = dict()

    def get_size(self):
        return self.size

    def get_snakes(self):
        return self.snakes

    def set_snakes(self,snakes):
        self.snakes = snakes

    def get_ladders(self):
        return self.ladders

    def set_ladders(self,ladders):
        self.ladders = ladders

    def get_player_pieces(self):
        return self.player_pieces

    def set_player_pieces(self,player_pieces):
        self.player_pieces = player_pieces