

from models.snake_ladder_player import Snake
from helper import get_random_numbers


class SnakeService:
    
    @staticmethod
    def create_snakes(count,snakes,snake_squares):
        while count != 0:
            while True:
                start_pos = get_random_numbers(2,99)
                end_pos = get_random_numbers(2,99)
                if end_pos < start_pos:
                    break
            snakes.append(Snake(start_pos, end_pos))
            snake_squares[start_pos] = end_pos
            count -= 1
            start_pos = 0
            end_pos = 0
        
        return snake_squares