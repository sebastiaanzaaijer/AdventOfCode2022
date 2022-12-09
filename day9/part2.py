from collections import namedtuple


def move_head(pos_head,direction):
    if direction == "L": return pos_head[0]-1,pos_head[1]
    if direction == "R": return pos_head[0]+1,pos_head[1]
    if direction == "U": return pos_head[0],pos_head[1]+1
    if direction == "D": return pos_head[0],pos_head[1]-1

def move_next(pos_head,pos):
    delta = pos_head[0]-pos[0],pos_head[1]-pos[1]
    if abs(delta[0]) <=1 and abs(delta[1]) <= 1:
        return pos
    return pos[0]+max(-1,min(delta[0],1)),pos[1]+max(-1,min(delta[1],1))

def solve_puzzle(puzzle_input):
    N = 10
    positions = [(0,0)]*N
    tail_positions = set()
    for move in puzzle_input.splitlines():
        direction,steps = move.split()
        for i in range(int(steps)):
            positions[0] = move_head(positions[0],direction)
            for i in range(1,N):
                positions[i] = move_next(positions[i-1],positions[i])
            tail_positions.add(positions[-1])
    return len(tail_positions)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))