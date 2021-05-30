

from models.board import SnakeAndLadderBoard
from services.dice_service import DiceService

class SnakeAndLadderService():
    
    DEFAULT_BOARD_SIZE = 100
    DEFAULT_NO_OF_DICES = 1

    def __init__(self, boardSize):
        self.snake_and_ladder_board = SnakeAndLadderBoard(boardSize)
        self.players = list()
        self.no_of_dices = self.DEFAULT_NO_OF_DICES;

    def setno_of_dices(self, no_of_dices):
        self.no_of_dices = no_of_dices

    def continue_till_last_player_wins(self, should_continue_till_last_player_wins):
        self.should_continue_till_last_player_wins = should_continue_till_last_player_wins

    def multiple_dice_roll_on_six(self, should_allow_multiple_dice_roll_on_six):
        self.should_allow_multiple_dice_roll_on_six = should_allow_multiple_dice_roll_on_six

    def set_players(self, players):
        self.initial_number_of_players = len(players)
        self.player_pieces = dict()
        for player in players:
            self.players.append(player)
            self.player_pieces[player.id] = 0

        self.snake_and_ladder_board.set_player_pieces(self.player_pieces)

    def set_snakes(self, snakes):
        self.snake_and_ladder_board.set_snakes(snakes)

    def set_ladders(self, ladders):
        self.snake_and_ladder_board.set_ladders(ladders)

    def get_position_from_snake_or_ladder(self, new_position):
        
        for snake in self.snake_and_ladder_board.get_snakes():
            if (snake.start == new_position):
                new_position = snake.end
        
        for ladder in self.snake_and_ladder_board.get_ladders():
            if (ladder.start == new_position):
                new_position = ladder.end

        return new_position


    def move_player(self,  player, positions):
        
        old_position = self.snake_and_ladder_board.get_player_pieces().get(player.id)
        new_position = old_position + positions

        boardSize = self.snake_and_ladder_board.get_size();

        if (new_position > boardSize):
            new_position = old_position
        else:
            new_position = self.get_position_from_snake_or_ladder(new_position);


        self.snake_and_ladder_board.get_player_pieces()[player.id] =  new_position

        print(f'{player.name}  rolled a positions and moved from  {old_position} to {new_position}')

    def get_rolled_dice_value(self):
        return DiceService.roll()

    def check_player_won(self,player):
        player_position = self.snake_and_ladder_board.get_player_pieces().get(player.id)
        winning_position = self.snake_and_ladder_board.get_size()
        return player_position == winning_position

    def start_game(self):
        while(len(self.players) != 0):
            for current_player in self.players:
                total_dice_value = self.get_rolled_dice_value()
                self.move_player(current_player, total_dice_value)
                if (self.check_player_won(current_player)):
                    print(current_player.name + " wins the game");
                    self.snake_and_ladder_board.get_player_pieces().pop(current_player.id)
                    self.players.remove(current_player)
        return self.players
