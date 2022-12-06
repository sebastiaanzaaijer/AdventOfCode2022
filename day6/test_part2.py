import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        self.assertEqual(solve_puzzle(example_input),19)

    def test_example_input2(self):
        example_input = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        self.assertEqual(solve_puzzle(example_input),23)

    def test_example_input3(self):
        example_input = "nppdvjthqldpwncqszvftbrmjlhg"
        self.assertEqual(solve_puzzle(example_input),23)

    def test_example_input4(self):
        example_input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        self.assertEqual(solve_puzzle(example_input),29)

    def test_example_input5(self):
        example_input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        self.assertEqual(solve_puzzle(example_input),26)
