from collections import defaultdict

def solve_puzzle(puzzle_input):
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
            
    return sum(dir_size for dir_size in directories.values() if dir_size <= 100000)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))