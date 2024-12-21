# read input
with open("input.txt", "r") as f:
    data = f.read().strip()

from functools import cache

@cache
def evol(val: str, gen: int) -> int:
    if gen == 0:
        return 1
    if val == "0":
        return evol("1", gen - 1)
    elif len(val) & 0x1 == 0:
        m = len(val) // 2
        return evol(str(int(val[:m])), gen - 1) + evol(str(int(val[m:])), gen - 1)
    val = str(int(val) * 2024)
    return evol(val, gen - 1)

# part 1
part1 = sum([evol(x, 25) for x in data.split()])
print(f"part1 = {part1}")

# part 2
part2 = sum([evol(x, 75) for x in data.split()])
print(f"part2 = {part2}")
