def compare_packets(pckt1,pckt2):
    if isinstance(pckt1,int) and isinstance(pckt2,int):
        if pckt1 < pckt2:
            return True
        if pckt1 > pckt2:
            return False
        return
    if isinstance(pckt1,list) and isinstance(pckt2,list):
        for i in range(len(pckt1)):
            if i >= len(pckt2):
                return False
            res = compare_packets(pckt1[i],pckt2[i])
            if not res is None:
                return res
        if len(pckt1) == len(pckt2):
            return # list of equal lengths are undecided
        return True
    if isinstance(pckt1,int):
        return compare_packets([pckt1],pckt2)
    if isinstance(pckt1,list):
        return compare_packets(pckt1,[pckt2])


def solve_puzzle(puzzle_input):
    total = 0
    for i,pair in enumerate(puzzle_input.split("\n\n"),1):
        right_order = compare_packets(*(eval(_) for _ in pair.split()))
        print(right_order)
        total += i*right_order
    return total

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))