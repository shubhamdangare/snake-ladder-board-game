
from helper import get_random_numbers, generate_random_even_numbers

from random import choice

class DiceService:
    
    @classmethod
    def roll(cls):
        return choice([DiceService.roll_normal,DiceService.roll_even])()
    
    @classmethod
    def roll_normal(cls):
        return get_random_numbers(1,6)
    
    @classmethod
    def roll_even(cls):
        return generate_random_even_numbers()