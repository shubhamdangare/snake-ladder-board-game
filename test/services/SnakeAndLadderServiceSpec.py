from unittest import TestCase
import unittest

from src.services.snake_ladder_service import SnakeAndLadderService
from src.services.snake_service import SnakeService
from src.services.ladder_service import LadderService
from src.services.player_service import PlayerService

class SnakeAndLadderServiceSpec(TestCase):
    
    def setUp(self):
        self.snake_squares = self.ladder_squares = {}
        self.count = 5
        self.noOfPlayers = 4
        self.snakes  = list()
        self.ladders = list()
        self.players = list()
        self.snake_squares = SnakeService.create_snakes(count=self.count,snakes = self.snakes,snake_squares= self.snake_squares)
        self.ladder_squares =  LadderService.create_ladders(count=self.count,ladders = self.ladders,ladder_squares = self.ladder_squares,
                                                            snake_squares= self.snake_squares)
        self.players = PlayerService.create_players(self.players,noOfPlayers=self.noOfPlayers)
       
        self.snakeAndLadderService = SnakeAndLadderService(100)
        self.snakeAndLadderService.set_players(self.players);
        self.snakeAndLadderService.set_snakes(self.snakes);
        self.snakeAndLadderService.set_ladders(self.ladders);

    def test_player_created(self):
       self.assertEqual(len(self.players),3)
    
    def test_snakes_created(self):
           self.assertEqual(len(self.snake_squares),10)
    
    def test_ladder_created(self):
           self.assertEqual(len(self.ladder_squares),10)
    
    def test__not_ladder_created(self):
           self.assertNotEqual(len(self.ladder_squares),9)
    
    def test_all_player_finished_game(self):
        self.players = self.snakeAndLadderService.start_game()
        self.assertEqual(len(self.players),0)
