def solve_puzzle(puzzle_input):
    for i in range(4,len(puzzle_input)+1):
        chrs = puzzle_input[i-4:i]
        if len(set(chrs)) == 4:
            break
    return i

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))