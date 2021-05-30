

from models.snake_ladder_player import Ladder
from helper import get_random_numbers


class LadderService:
    
    @staticmethod
    def create_ladders(count,ladders,ladder_squares,snake_squares):
        while count != 0:
            while True:
                start_pos = get_random_numbers(1,99)
                end_pos = get_random_numbers(1,99)
                if end_pos < start_pos and not snake_squares.get(end_pos):
                    break
            ladders.append(Ladder(end_pos, start_pos))
            ladder_squares[end_pos] = start_pos
            count -= 1
            start_pos = 0
            end_pos = 0
        return ladder_squares