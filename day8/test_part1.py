import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = \
"""30373
25512
65332
33549
35390"""
        self.assertEqual(solve_puzzle(example_input),21)
