from functools import cmp_to_key

def compare_packets(pckt1,pckt2):
    if isinstance(pckt1,int) and isinstance(pckt2,int):
        if pckt1 < pckt2:
            return -1
        if pckt1 > pckt2:
            return 1
        return
    if isinstance(pckt1,list) and isinstance(pckt2,list):
        for i in range(len(pckt1)):
            if i >= len(pckt2):
                return 1
            res = compare_packets(pckt1[i],pckt2[i])
            if not res is None:
                return res
        if len(pckt1) == len(pckt2):
            return # list of equal lengths are undecided
        return -1
    if isinstance(pckt1,int):
        return compare_packets([pckt1],pckt2)
    if isinstance(pckt1,list):
        return compare_packets(pckt1,[pckt2])


def solve_puzzle(puzzle_input):
    packets = [eval(_) for _ in puzzle_input.splitlines() if _]
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(compare_packets))
    return ((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
    

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))