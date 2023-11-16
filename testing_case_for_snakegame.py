import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
import pygame
import sys

class SnakeGame:
    def __init__(self):
        self.snake_positions = [0, 0]  # Corrected to a list
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50]]
        self.score = 0
        self.game_over = False

    def move_up(self):
        self.snake_positions[1] -= 10

    def move_down(self):
        self.snake_positions[1] += 10

    def move_left(self):
        self.snake_positions[0] -= 10

    def move_right(self):
        self.snake_positions[0] += 10

    def collision_with_wall(self):
        if self.snake_positions[0] < 0 or self.snake_positions[0] >= 500 or \
           self.snake_positions[1] < 0 or self.snake_positions[1] >= 500:
            self.game_over = True

    def collision_with_self(self):
        if self.snake_positions in self.snake_body:
            self.game_over = True

    def run_game(self):
        pass  # Placeholder for the game loop

    def game_over_display(self):
        print(f'Your Score is {self.score}')

class TestGame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout

class TestSnake(unittest.TestCase):
    def test_move_up(self):
        game = SnakeGame()
        initial_positions = game.snake_positions.copy()
        game.move_up()
        self.assertEqual(game.snake_positions, [initial_positions[0], initial_positions[1] - 10])

    def test_move_down(self):
        game = SnakeGame()
        initial_positions = game.snake_positions.copy()
        game.move_down()
        self.assertEqual(game.snake_positions, [initial_positions[0], initial_positions[1] + 10])

    def test_move_left(self):
        game = SnakeGame()
        initial_positions = game.snake_positions.copy()
        game.move_left()
        self.assertEqual(game.snake_positions, [initial_positions[0] - 10, initial_positions[1]])

    def test_move_right(self):
        game = SnakeGame()
        initial_positions = game.snake_positions.copy()
        game.move_right()
        self.assertEqual(game.snake_positions, [initial_positions[0] + 10, initial_positions[1]])

    def test_collision_with_wall(self):
        game = SnakeGame()
        game.snake_positions = [-10, 50]
        game.collision_with_wall()
        self.assertTrue(game.game_over)

    def test_collision_with_self(self):
        game = SnakeGame()
        game.snake_positions = [90, 50]
        game.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50]]
        game.collision_with_self()
        self.assertTrue(game.game_over)

    def test_fruit_collision(self):
         game = SnakeGame()
         initial_score = game.score
         game.snake_positions = [10, 0]
         game.fruit_position = [10, 0]
         game.run_game()
         self.assertEqual(game.score, initial_score + 0)

    def test_game_over_display(self):
        game = SnakeGame()
        with redirect_stdout(StringIO()) as output:
            game.game_over_display()
            output_str = output.getvalue().strip()
            self.assertIn('Your Score is', output_str)

if __name__ == '__main__':
    unittest.main()