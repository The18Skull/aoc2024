# read input
with open("input.txt", "r") as f:
    data = f.read()

reports = []
for line in data.splitlines():
    arr = list(map(int, line.split(" ")))
    reports.append(arr)

def safe_unsafe(reports: list[list[int]], max_fails: int = 1) -> tuple[int, int]:
    safe = unsafe = 0
    for rep in reports:
        neg = (rep[1] - rep[0]) < 0
        fails = 0
        for (a, b) in zip(rep[:-1], rep[1:]):
            d = b - a
            if abs(d) not in (1, 2, 3) or d > 0 and neg or d < 0 and not neg:
                fails += 1
            if fails >= max_fails:
                break
        if fails < max_fails:
            safe += 1
        else:
            unsafe += 1
    return safe, unsafe

# part 1
safe, unsafe = safe_unsafe(reports, max_fails=1)
print(f"part1 = {safe}")

# part 2
safe, unsafe = safe_unsafe(reports, max_fails=2)
print(f"part2 = {safe}")
