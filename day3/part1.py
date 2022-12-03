def priority_value(item):
    ascii = ord(item)
    return ascii - 64 + 26 if ascii < 91 else ascii - 96

def get_score(items):
    nr_items = len(items)
    items_in_first_compartment = items[:nr_items//2]
    items_in_second_compartment = items[nr_items//2:]
    duplicate_item = (set(items_in_first_compartment) & set(items_in_second_compartment)).pop()
    return priority_value(duplicate_item)

def solve_puzzle(puzzle_input):
    return sum(get_score(inventory) for inventory in puzzle_input.splitlines())


if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))