from collections import namedtuple


def move_head(pos_head,direction):
    if direction == "L": return pos_head[0]-1,pos_head[1]
    if direction == "R": return pos_head[0]+1,pos_head[1]
    if direction == "U": return pos_head[0],pos_head[1]+1
    if direction == "D": return pos_head[0],pos_head[1]-1

def move_tail(pos_head,pos_tail):
    delta = pos_head[0]-pos_tail[0],pos_head[1]-pos_tail[1]
    if abs(delta[0]) <=1 and abs(delta[1]) <= 1:
        return pos_tail
    return pos_tail[0]+max(-1,min(delta[0],1)),pos_tail[1]+max(-1,min(delta[1],1))

def solve_puzzle(puzzle_input):
    pos_head = 0,0
    pos_tail = 0,0
    tail_positions = set()
    for move in puzzle_input.splitlines():
        direction,steps = move.split()
        for i in range(int(steps)):
            pos_head = move_head(pos_head,direction)
            pos_tail = move_tail(pos_head,pos_tail)
            tail_positions.add(pos_tail)
    return len(tail_positions)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))