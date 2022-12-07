from collections import defaultdict

def solve_puzzle(puzzle_input):
    TOTAL_SPACE = 70000000
    REQUIRED_SPACE = 30000000

    directories = defaultdict(int)
    current_directory = ""
    for line in puzzle_input.splitlines():
        if line.startswith("$"): # command
            tokens = line[2:].split()
            if tokens[0] == "cd":
                if tokens[1] == "..":
                    current_directory = current_directory.rsplit("/",1)[0]
                elif tokens[1] == "/":
                    current_directory = ""
                else:
                    current_directory += "/"+tokens[1]
        else: # listing
            size_or_type,name = line.split()
            if size_or_type != "dir":
                size = int(size_or_type)
                dirs = current_directory.split("/")
                for i in range(len(dirs)):
                    directories["/".join(dirs[:i+1])] += size
    minimal_directory_size = REQUIRED_SPACE-(TOTAL_SPACE-directories[""])
    return next(dir_size for dir_size in sorted(directories.values()) if dir_size >= minimal_directory_size)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))