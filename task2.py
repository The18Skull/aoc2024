# read input
with open("input2.txt", "r") as f:
    data = f.read()

reports = []
for line in data.splitlines():
    data = list(map(int, line.split(" ")))
    reports.append(data)

# part 1
safe = unsafe = 0
for rep in reports:
    neg = (rep[1] - rep[0]) < 0
    for (a, b) in zip(rep[:-1], rep[1:]):
        d = b - a
        if abs(d) not in (1, 2, 3) or d > 0 and neg or d < 0 and not neg:
            unsafe += 1
            break
    else:
        safe += 1
print(f"safe = {safe}, unsafe = {unsafe}")

# part 2
safe = unsafe = 0
for rep in reports:
    neg = (rep[1] - rep[0]) < 0
    fails = 0
    for (a, b) in zip(rep[:-1], rep[1:]):
        d = b - a
        if abs(d) not in (1, 2, 3) or d > 0 and neg or d < 0 and not neg:
            fails += 1
    if fails < 2:
        safe += 1
    else:
        unsafe += 1
print(f"safe = {safe}, unsafe = {unsafe}")
