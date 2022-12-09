import unittest

from .part2 import solve_puzzle

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
        self.assertEqual(solve_puzzle(example_input),1)

    def test_example_input2(self):
        example_input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
        self.assertEqual(solve_puzzle(example_input),36)

