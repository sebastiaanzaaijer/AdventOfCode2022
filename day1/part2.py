def solve_puzzle(puzzle_input):
    return sum(sorted(sum(map(int,block.splitlines())) for block in puzzle_input.split("\n\n"))[-3:])

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))