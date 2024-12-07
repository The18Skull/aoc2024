# read input
with open("input.txt", "r") as f:
    data = f.read()

equations = []
for line in data.splitlines():
    target, variables = line.split(": ", 1)
    equations.append((int(target), list(map(int, variables.split(" ")))))

from itertools import product

def calc(equations: list[tuple[int, list[int]]], operations: str) -> int:
    ans = 0
    for (target, variables) in equations:
        for ops in product(operations, repeat=len(variables) - 1):
            res, *other = variables
            for x, op in zip(other, ops):
                if op == "+":
                    res += x
                elif op == "*":
                    res *= x
                elif op == "|":
                    res = int(str(res) + str(x))
            if res == target:
                ans += target
                break
    return ans

# part 1
part1 = calc(equations, operations="+*")
print(f"part1 = {part1}")

# part 2
part2 = calc(equations, operations="+*|")
print(f"part2 = {part2}")
