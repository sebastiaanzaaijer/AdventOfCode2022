
class Node:
    def __init__(self,v,n,p):
        self.i = v
        self.n = n
        self.p = p

    def move_after(self,after):
        if self == after:
            return
        before = after.n
        self.p.n,self.n.p = self.n,self.p

        self.p = after
        self.n = after.n

        before.p = self
        after.n = self

    def move_steps(self,n):
        node = self.node_at_offset(n)
        self.move_after(node)

    def node_at_offset(self,n):
        node = self
        for _ in range(n):
            node = node.n
        return node        

    def __repr__(self) -> str:
        return f"{self.i} {self.n.v} {self.p.v} |"

    def __str__(self) -> str:
        return self.__repr__()

class Message:
    def __init__(self,values):
        self.index0 = values.index(0)
        self.values = values
        self.nodes = {i:Node(i,None,None) for i in range(len(values))}
        for i in range(len(values)):
            self.nodes[i].p = self.nodes[(i-1)%len(values)]
            self.nodes[i].n = self.nodes[(i+1)%len(values)]

    def decode(self):
        for ni in self.nodes:
            self.nodes[ni].move_steps(self.values[ni] % (len(self.values)-1))

    def show(self):
        node = self.nodes[0]
        for i in range(len(self.values)):
            print(self.values[node.i],",",end="")
            node = node.n
        print("")
    
    def coordinates(self):
        start = self.nodes[self.index0]
        return sum(self.values[(start.node_at_offset(offset % len(self.values))).i] for offset in range(1000,3001,1000))

def solve_puzzle(puzzle_input):
    message = Message(list(map(int,puzzle_input.splitlines())))
    message.decode()
    return message.coordinates()

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))