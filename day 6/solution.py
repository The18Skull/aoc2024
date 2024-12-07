# read input
with open("input.txt", "r") as f:
    data = f.read()

guard = 0, 0
array: list[list[str]] = []
for line in data.splitlines():
    if "^" in line:
        guard = line.index("^"), len(array) - 1
        line = line.replace("^", ".", 1)
    arr = list(line)
    array.append(arr)

from itertools import cycle

def get_direction():
    directions = cycle(((0, -1), (1, 0), (0, 1), (-1, 0)))
    while True:
        cur = next(directions)
        while True:
            val = (yield cur)
            if val:
                break

def check_out_of_bounds(val: tuple[int, int] | int, max: int = len(array)) -> bool:
    if isinstance(val, tuple):
        return any(check_out_of_bounds(x, max) for x in val)
    if val < 0 or val >= max:
        return True
    return False

def calculate_path(new_map: list[list[str]], guard: tuple[int, int]) -> list[tuple[int, int]]:
    direction = get_direction()

    path = []
    while True:
        dx, dy = next(direction)

        x, y = guard
        if not check_out_of_bounds((x + dx, y + dy)) and new_map[y + dy][x + dx] in ("#", "O") and new_map[y][x] == "+":
            return []

        if new_map[y][x] == "." and dx != 0:
            new_map[y][x] = "-"
        elif new_map[y][x] == "." and dy != 0:
            new_map[y][x] = "|"
        elif new_map[y][x] == "|" and dx != 0:
            new_map[y][x] = "+"
        elif new_map[y][x] == "-" and dy != 0:
            new_map[y][x] = "+"
        path.append((x, y))

        while not check_out_of_bounds((x + dx, y + dy)) and new_map[y + dy][x + dx] in ("#", "O"):
            dx, dy = direction.send(1)
            new_map[y][x] = "+"
        x += dx; y += dy

        if check_out_of_bounds((x, y)):
            break
        guard = x, y

    return path

# part 1
new_map = [x.copy() for x in array]
path = calculate_path(new_map, guard)
part1 = len(set(path))
print(f"part1 = {part1}")

# part 2
obs = []
for i, pos in enumerate(set(path)):
    if pos == guard:
        continue

    x, y = pos
    new_map = [x.copy() for x in array]
    new_map[y][x] = "O"

    new_path = calculate_path(new_map, guard)
    if not new_path:
        obs.append((x, y))
part2 = len(set(obs))
print(f"part2 = {part2}")
