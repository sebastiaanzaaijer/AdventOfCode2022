import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = \
"""A Y
B X
C Z"""
        self.assertEqual(solve_puzzle(example_input),12)
