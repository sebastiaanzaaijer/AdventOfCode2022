from io import StringIO

class CPU:
    def __init__(self,program) -> None:
        self.program = program

    def __iter__(self):
        self.X = 1
        self.counter = 0
        self.wait = 0
        self.add = 0
        self.instructions = StringIO(self.program)
        return self
        
    def __next__(self):
        if self.wait == 0:
            self.X += self.add
            self.add = 0
            instruction = next(self.instructions).strip().split()
            if instruction[0] == "addx":
                self.wait = 2
                self.add = int(instruction[1])
        self.wait = max(self.wait-1,0)

        return self.X

            


def solve_puzzle(puzzle_input):
    signal_strength = 0
    for i,regx in enumerate(CPU(puzzle_input),1):
        if (i+20) % 40 == 0:
            signal_strength += i*regx
    return signal_strength

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))