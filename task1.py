# read input
with open("input1.txt", "r") as f:
    data = f.read()

left = []; right = []
for line in data.splitlines():
    a, b = map(int, line.split(" ", 1))
    left.append(a); right.append(b)

# part 1
arr1 = sorted(left); arr2 = sorted(right)
part1 = sum(abs(a - b) for (a, b) in zip(arr1, arr2))
print(f"part1 = {part1}")

# part 2
part2 = sum([x * right.count(x) for x in left])
print(f"part2 = {part2}")
