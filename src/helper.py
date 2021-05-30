

from random import randint, choice, randrange
import string

def get_random_numbers(start = 1 , end = 1):
    return randint(start,end)

def id_generator(size=6, chars= string.ascii_uppercase + string.digits):
    return ''.join(choice(chars) for _ in range(size))

def generate_random_even_numbers():
    return randrange(1, 6, 2)