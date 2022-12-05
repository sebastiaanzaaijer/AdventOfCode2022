from collections import defaultdict

def make_move(stacks,nr,from_,to_):
    crane = []
    for i in range(nr):
        crane.append(stacks[from_].pop())
    for crate in crane:
        stacks[to_].append(crate)


def solve_puzzle(puzzle_input):
    lines = puzzle_input.splitlines()
    stacks = defaultdict(list)
    moves = []
    while True:
        l = lines.pop(0)
        for i,chr in enumerate(l[1::4],1):
            if chr != " ":
                stacks[i].append(chr)
        if l.strip().startswith("1"): break
    for stack in stacks.values():
        stack.reverse()
    lines.pop(0)
    for l in lines:
        nr, from_, to_ = map(int,l.replace("move","").replace("from","").replace("to","").split())
        make_move(stacks,nr,from_,to_)
    return "".join(stacks[k][-1] for k in sorted(stacks))

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))