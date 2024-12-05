# read input
with open("input.txt", "r") as f:
    data = f.read()

rules: dict[int, list[int]] = {}
updates: list[list[int]] = []
for line in data.splitlines():
    if "|" in line:
        a, b = map(int, line.split("|", 1))
        rules.setdefault(a, []).append(b)
    elif "," in line:
        updates.append(list(map(int, line.split(","))))

def is_correct(update: list[int]) -> bool:
    for i in range(len(update) - 1, 0, -1):
        rule = rules.get(update[i], [])
        for x in rule:
            try:
                update.index(x, 0, i)
                return False
            except ValueError:
                pass
    return True

correct: list[list[int]] = []
incorrect: list[list[int]] = []
for update in updates:
    if is_correct(update):
        correct.append(update)
    else:
        incorrect.append(update)

# part 1
part1 = sum([update[len(update) // 2] for update in correct])
print(f"part1 = {part1}")

# part 2
for update in incorrect:
    while not is_correct(update):
        for i in range(len(update) - 1, 0, -1):
            rule = rules.get(update[i], [])
            for x in rule:
                try:
                    j = update.index(x, 0, i)
                    update.insert(i, update.pop(j))
                    break
                except ValueError:
                    pass
            else:
                continue
            break
part2 = sum([update[len(update) // 2] for update in incorrect])
print(f"part2 = {part2}")
