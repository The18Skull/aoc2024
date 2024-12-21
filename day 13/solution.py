# read input
with open("input.txt", "r") as f:
    data = f.read().strip()

games: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]] = []
for block in data.split("\n\n"):
    game = []
    for line in block.split("\n"):
        _, r = line.split(": ", 1)
        x, y = map(lambda x: int(x[2:]), r.split(", ", 1))
        game.append((x, y))
    games.append(tuple(game))

def play_game(a: tuple[int, int], b: tuple[int, int], g: tuple[int, int]) -> int | None:
    # Cramer's rule
    d = a[0] * b[1] - a[1] * b[0]
    if d == 0:
        return None

    d1 = g[0] * b[1] - g[1] * b[0]
    d2 = a[0] * g[1] - a[1] * g[0]
    if d1 % d or d2 % d:
        return None

    x1, x2 = d1 // d, d2 // d
    return x1 * 3 + x2 * 1

# part 1
part1 = 0
for (a, b, g) in games:
    c = play_game(a, b, g)
    if c is not None:
        part1 += c
print(f"part1 = {part1}")

# part 2
offset = 10000000000000

part2 = 0
for (a, b, g) in games:
    c = play_game(a, b, (g[0] + offset, g[1] + offset))
    if c is not None:
        part2 += c
print(f"part2 = {part2}")
