# read input
with open("input.txt", "r") as f:
    data = f.read().strip()

buffer = []

cur = 0
for i, x in enumerate(map(int, data)):
    if i & 0x1:
        buffer.extend(["."] * x)
    else:
        buffer.extend([cur] * x)
        cur += 1

# part 1
i = 0
buf = buffer[:]
while i < len(buf):
    if buf[i] != ".":
        i += 1
        continue
    buf[i] = buf.pop()

part1 = 0
for i, x in enumerate(buf):
    if buf[i] == ".":
        continue
    part1 += x * i
print(f"part1 = {part1}")

# part 2
buf = buffer[:]
for x in range(len(data) // 2, 0, -1):
    i, c = buf.index(x), buf.count(x)

    j = None
    for k in range(i + 1):
        if buf[k] == "." and j is None:
            j = k
        if j is not None:
            if k - j >= c:
                break
            elif buf[k] != ".":
                j = None
    if j is not None and k - j >= c:
        for o in range(i, i + c):
            buf[j], buf[o] = buf[o], buf[j]
            j += 1

part2 = 0
for i, x in enumerate(buf):
    if buf[i] == ".":
        continue
    part2 += x * i
print(f"part2 = {part2}")
