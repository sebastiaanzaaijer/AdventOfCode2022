def solve_puzzle(puzzle_input):
    elevations = []
    distances = []
    start_location = None
    end_location = None
    for rowid,row in enumerate(puzzle_input.splitlines()):
        row_elevations = []
        for colid,chr in enumerate(row):
            height = ord(chr)
            if chr == "S":
                start_location = rowid,colid
                height = ord("a")
            if chr == "E":
                end_location = rowid,colid
                height = ord("z")
            row_elevations.append(height)
        elevations.append(row_elevations)
        distances.append([-1]*len(row))
    to_visit = [end_location]
    distances[end_location[0]][end_location[1]] = 0
    nrows = len(distances)
    ncols = len(distances[0])
    while to_visit:
        visit_next = []
        for point in to_visit:
            height = elevations[point[0]][point[1]]
            distance = distances[point[0]][point[1]]
            for offset in (-1,0),(1,0),(0,-1),(0,1):
                rowid = point[0]+offset[0]
                colid = point[1]+offset[1]
                if 0 <= rowid < nrows and 0 <= colid < ncols:
                    if height-elevations[rowid][colid] <= 1:
                        if (rowid,colid) == start_location:
                            return distance + 1 # we can stop when the start was reached
                        if distances[rowid][colid] < 0:
                            distances[rowid][colid] = distance + 1
                            visit_next.append((rowid,colid))
        to_visit = visit_next 

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))