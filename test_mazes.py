# coding: utf-8

import unittest

import json

import mazes

class TestMazeSolver(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generate_square_maze(self):
        maze = mazes.build_maze(10, 10)
        solution = mazes.solve_maze(maze)
        self.assertIsNotNone(solution)

    def test_generate_rectagle_maze(self):
        maze = mazes.build_maze(10, 20)
        solution = mazes.solve_maze(maze)
        self.assertIsNotNone(solution)

    def test_compare_to_existing_data(self):
        with open('maze_fixtures.json', 'r') as handle:
            fixtures = json.load(handle)

        solution = mazes.solve_maze(fixtures['maze'])
        
        self.assertEqual(solution, fixtures['solution'])

if __name__ == '__main__':
    unittest.main()