from turtle import pu


snafu_values = {
    "=" : -2,
    "-" : -1,
    "0" : 0,
    "1" : 1,
    "2" : 2,
}

value_to_snafu = {
    0: "0",
    1: "1",
    2: "2",
    3: "=",
    4: "-",
}


def snafu_to_int(snafu):
    return sum(snafu_values[c]*5**i for i,c in enumerate(snafu[::-1]))

def int_to_snafu(nr):
    if nr == 0:
        return "0"
    snafu = ""
    while nr:
        value = (nr) % 5
        snafu = value_to_snafu[value] + snafu
        nr //= 5
        if value > 2:
            nr += 1
    return snafu


def solve_puzzle(puzzle_input):
    return int_to_snafu(sum(snafu_to_int(l) for l in puzzle_input.splitlines()))

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))