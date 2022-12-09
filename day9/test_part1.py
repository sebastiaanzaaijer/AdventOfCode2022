import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
        self.assertEqual(solve_puzzle(example_input),13)
