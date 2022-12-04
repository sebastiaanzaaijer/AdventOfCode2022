def solve_puzzle(puzzle_input):
    overlaps = 0
    for l in puzzle_input.splitlines():
        elf1,elf2 = l.split(",")
        elf1 = tuple(map(int,elf1.split("-")))
        elf2 = tuple(map(int,elf2.split("-")))
        overlaps += (min(elf1[1],elf2[1]) - max(elf1[0],elf2[0])) >= 0
    return overlaps

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))