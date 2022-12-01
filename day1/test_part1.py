import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = \
"""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
        self.assertEqual(solve_puzzle(example_input),24000)
