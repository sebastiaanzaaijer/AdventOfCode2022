def solve_puzzle(puzzle_input):
    visible_trees = set()
    rows = puzzle_input.splitlines()
    for rowid,row in enumerate(rows):
        current_max = -1
        for colid,chr in enumerate(row): # process left to right
            height = int(chr)
            if height > current_max:
                visible_trees.add((rowid,colid))
                current_max = height
            if height == 9: break

        current_max = -1
        for colid,chr in enumerate(reversed(row),start=-len(row)+1): # process left to right
            colid = abs(colid)
            height = int(chr)
            if height > current_max:
                visible_trees.add((rowid,colid))
                current_max = height
            if height == 9: break

    # reverse rows and columns
    columns = zip(*puzzle_input.splitlines())
    for colid,col in enumerate(columns):
        current_max = -1
        for rowid,chr in enumerate(col): # process left to right
            height = int(chr)
            if height > current_max:
                visible_trees.add((rowid,colid))
                current_max = height
            if height == 9: break
 
        current_max = -1
        for rowid,chr in enumerate(reversed(col),start=-len(col)+1): # process left to right
            rowid = abs(rowid)
            height = int(chr)
            if height > current_max:
                visible_trees.add((rowid,colid))
                current_max = height
            if height == 9: break

    return len(visible_trees)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))