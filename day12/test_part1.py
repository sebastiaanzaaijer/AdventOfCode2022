import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
        self.assertEqual(solve_puzzle(example_input),31)
