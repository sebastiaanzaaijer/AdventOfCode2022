from itertools import takewhile

def look_left(tree_grid,rowid,colid):
    height = tree_grid[rowid][colid]
    nr = 0
    for ci in range(colid-1,-1,-1):
        current_height = tree_grid[rowid][ci]
        nr += 1
        if current_height >= height:
            return nr
    return nr

def look_right(tree_grid,rowid,colid):
    height = tree_grid[rowid][colid]
    nr = 0
    for ci in range(colid+1,len(tree_grid[0])):
        current_height = tree_grid[rowid][ci]
        nr += 1
        if current_height >= height:
            return nr
    return nr   

def look_up(tree_grid,rowid,colid):
    height = tree_grid[rowid][colid]
    nr = 0
    for  ri in range(rowid-1,-1,-1):
        current_height = tree_grid[ri][colid]
        nr += 1
        if current_height >= height:
            return nr
    return nr   

def look_down(tree_grid,rowid,colid):
    height = tree_grid[rowid][colid]
    nr = 0
    for  ri in range(rowid+1,len(tree_grid)):
        current_height = tree_grid[ri][colid]
        nr += 1
        if current_height >= height:
            return nr
    return nr  
# def look_up(tree_grid,rowid,colid):



def solve_puzzle(puzzle_input):
    tree_grid = tuple(tuple(map(int,l)) for l in puzzle_input.splitlines())

    max_vis_score = 0
    for rowid in range(1,len(tree_grid)-1):
        for colid in range(1,len(tree_grid[0])-1):
            left = look_left(tree_grid,rowid,colid)
            right = look_right(tree_grid,rowid,colid)
            top = look_up(tree_grid,rowid,colid)
            bottom = look_down(tree_grid,rowid,colid)
            max_vis_score = max(max_vis_score,
                left*right*top*bottom)
    return max_vis_score

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))