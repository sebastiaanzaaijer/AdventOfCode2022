import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """1
2
-3
3
-2
0
4"""
        self.assertEqual(solve_puzzle(example_input),3)
