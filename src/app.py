

from services.snake_ladder_service import SnakeAndLadderService
from services.snake_service import SnakeService
from services.ladder_service import LadderService
from services.player_service import PlayerService

def main():
        snake_squares = ladder_squares = {}
        count = 5
        noOfPlayers = 4
        snakes  = list()
        ladders = list()
        players = list()
        
        snake_squares = SnakeService.create_snakes(count=count,snakes = snakes,snake_squares= snake_squares)
        
        ladder_squares =  LadderService.create_ladders(count=count,ladders = ladders,ladder_squares = ladder_squares,snake_squares= snake_squares)
        
        players = PlayerService.create_players(players,noOfPlayers=noOfPlayers)
       
        snakeAndLadderService = SnakeAndLadderService(100)
        snakeAndLadderService.set_players(players);
        snakeAndLadderService.set_snakes(snakes);
        snakeAndLadderService.set_ladders(ladders);
        snakeAndLadderService.start_game();

if __name__ == '__main__':
    main()