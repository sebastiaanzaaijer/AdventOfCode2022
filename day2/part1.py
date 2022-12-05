
score = {
    "A X" : 1 + 3,
    "A Y" : 2 + 6,
    "A Z" : 3 + 0,
    "B X" : 1 + 0,
    "B Y" : 2 + 3,
    "B Z" : 3 + 6,
    "C X" : 1 + 6,
    "C Y" : 2 + 0,
    "C Z" : 3 + 3,
}


def solve_puzzle(puzzle_input):
    return sum(score[l] for l in puzzle_input.splitlines())

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))