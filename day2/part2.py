score = {
    "A X" : 3 + 0,
    "A Y" : 1 + 3,
    "A Z" : 2 + 6,
    "B X" : 1 + 0,
    "B Y" : 2 + 3,
    "B Z" : 3 + 6,
    "C X" : 2 + 0,
    "C Y" : 3 + 3,
    "C Z" : 1 + 6,
}


def solve_puzzle(puzzle_input):
    return sum(score[l] for l in puzzle_input.splitlines())

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))