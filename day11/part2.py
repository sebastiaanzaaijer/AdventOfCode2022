from operator import add,mul

op = {
    "*" : mul,
    "+" : add,
}

def generate_monkey(nr,operation,to_monkey,devisors_product):
    def f(monkies):
        while len(monkies[nr]["inventory"]) > 0:
            item = operation(monkies[nr]["inventory"].pop(0))
            monkies[to_monkey(item)]["inventory"].append(item % devisors_product)
            monkies[nr]["inspection_count"] += 1
        return monkies
    return f


def generate_operation(expr):
    def f(old):
        loc = {"old" : old}
        exec(expr,{},loc)
        return loc["new"]
    return f

def generate_to_monkey(devisor,if_true,if_false):
    def f(x):
        if x % devisor == 0: return if_true
        return if_false
    return f

def solve_puzzle(puzzle_input):
    monkey_inputs = puzzle_input.split("\n\n")
    monkeys = []

    # calculate procut of all devisors
    # taking modulo avoids item size going too large
    # doesn't effect the devisor test
    devisors_product = 1
    for i,input in enumerate(monkey_inputs):
        properties = input.splitlines()
        devisors_product *= int(properties[3].split()[-1])

    for i,input in enumerate(monkey_inputs):
        properties = input.splitlines()
        devisor = int(properties[3].split()[-1])
        if_true = int(properties[4].split()[-1])
        if_false = int(properties[5].split()[-1])
        operation = generate_operation(properties[2].split(":")[-1].strip())
        to_monkey = generate_to_monkey(devisor,if_true,if_false)
        monkeys.append({
            "inventory" : list(map(int,properties[1].split(":")[-1].strip().split(", "))),
            "behaviour" : generate_monkey(i,operation,to_monkey,devisors_product),
            "devisor" : devisor,
            "inspection_count" : 0,
        })
    for i in range(10_000):
        for monkey in monkeys:
            monkeys = monkey["behaviour"](monkeys)
    counts = sorted([monkey["inspection_count"] for monkey in monkeys])
    return counts[-1]*counts[-2]

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))