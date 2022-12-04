def solve_puzzle(puzzle_input):
    full_overlaps = 0
    for l in puzzle_input.splitlines():
        elf1,elf2 = l.split(",")
        elf1 = tuple(map(int,elf1.split("-")))
        elf2 = tuple(map(int,elf2.split("-")))
        full_overlaps += (elf1[0] >= elf2[0] and  elf1[1] <= elf2[1]) or (elf2[0] >= elf1[0] and  elf2[1] <= elf1[1])
    return full_overlaps

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))