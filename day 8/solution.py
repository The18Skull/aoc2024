# read input
with open("input.txt", "r") as f:
    data = f.read()

array: list[list[str]] = []
for line in data.splitlines():
    arr = list(line)
    array.append(arr)

frequencies = {"#": []}
for i in range(len(array)):
    for j in range(len(array[i])):
        pos = array[i][j]
        if pos == ".":
            continue
        frequencies.setdefault(pos, []).append((j, i))

def check_out_of_bounds(val: tuple[int, int] | int, max: int = len(array)) -> bool:
    if isinstance(val, tuple):
        return any(check_out_of_bounds(x, max) for x in val)
    if val < 0 or val >= max:
        return True
    return False

from itertools import permutations

new_map = [x.copy() for x in array]

# part 1
frequencies["#"].clear()
for freq, poses in frequencies.items():
    if freq == "#":
        continue
    for a, b in permutations(poses, 2):
        x = a[0] + (b[0] - a[0]) * 2
        y = a[1] + (b[1] - a[1]) * 2
        if check_out_of_bounds((x, y)):
            continue
        if new_map[y][x] == ".":
            new_map[y][x] = "#"
        frequencies["#"].append((x, y))
part1 = len(set(frequencies["#"]))
print(f"part1 = {part1}")

# part 2
frequencies["#"].clear()
for freq, poses in frequencies.items():
    if freq == "#":
        continue
    for a, b in permutations(poses, 2):
        dx, dy = b[0] - a[0], b[1] - a[1]
        x, y = a[0] + dx, a[1] + dy

        while not check_out_of_bounds((x, y)):
            if new_map[y][x] == ".":
                new_map[y][x] = "#"
            frequencies["#"].append((x, y))
            x += dx; y += dy
part2 = len(set(frequencies["#"]))
print(f"part2 = {part2}")
