from part1 import priority_value

def group_priority(group):
    return priority_value(set(group[0]).intersection(*group[1:]).pop())


def solve_puzzle(puzzle_input):
    inventories = puzzle_input.splitlines()
    return sum(group_priority(group) for group in zip(inventories[::3],inventories[1::3],inventories[2::3]))

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))