# read input
with open("input.txt", "r") as f:
    data = f.read().strip()

array: list[list[int]] = []
for line in data.splitlines():
    arr = list(map(int, line))
    array.append(arr)

def check_paths(new_map: list[list[int]], x: int, y: int, val: int, ends: set[tuple[int, int]] | None) -> int:
    if new_map[y][x] != val:
        return 0
    if val == 9:
        if ends is not None:
            if (x, y) in ends:
                return 0
            ends.add((x, y))
        return 1
    val += 1

    res = 0
    if x > 0:
        res += check_paths(new_map, x - 1, y, val, ends)
    if x < len(new_map[y]) - 1:
        res += check_paths(new_map, x + 1, y, val, ends)
    if y > 0:
        res += check_paths(new_map, x, y - 1, val, ends)
    if y < len(new_map) - 1:
        res += check_paths(new_map, x, y + 1, val, ends)
    return res

# part 1
part1 = 0
for i, line in enumerate(array):
    for j, x in enumerate(line):
        if x != 0:
            continue
        part1 += check_paths(array, j, i, 0, set())
print(f"part1 = {part1}")

# part 2
part2 = 0
for i, line in enumerate(array):
    for j, x in enumerate(line):
        if x != 0:
            continue
        part2 += check_paths(array, j, i, 0, None)
print(f"part2 = {part2}")
