def plot_cave(cave,settled_sand):
    xmin, *_, xmax= sorted(_[0] for _ in cave | settled_sand)
    ymin, *_, ymax= sorted(_[1] for _ in cave | settled_sand)
    for y in range(ymin,ymax+1):
        for x in range(xmin,xmax+1):
            if (x,y) in cave:
                print("#",end="")
            elif (x,y) in settled_sand:
                print("o",end="")
            else:
                print(" ",end="")
        print()

def solve_puzzle(puzzle_input):
    cave = set()
    settled_sand = set()
    bottom = 0
    right = 0
    for line in puzzle_input.splitlines():
        points = tuple(tuple(map(int,_.split(","))) for _ in line.split(" -> "))
        for p1,p2 in zip(points,points[1:]):
            x1,x2 = (p1[0],p2[0]) if p1[0]<p2[0] else (p2[0],p1[0])
            y1,y2 = (p1[1],p2[1]) if p1[1]<p2[1] else (p2[1],p1[1])
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    cave.add((x,y))
                    bottom = max(bottom,y2)
                    right = max(bottom,y2)

    move_order = (0,1),(-1,1),(1,1) 
    sand = (500,0)
    while sand[1] <= bottom:
        for move in move_order:
            next_position = sand[0]+move[0],sand[1]+move[1]
            if not next_position in (cave | settled_sand):
                sand = next_position
                break
        if sand != next_position:
            settled_sand.add(sand)
            sand = (500,0)
    # plot_cave(cave,settled_sand)
    return len(settled_sand)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))