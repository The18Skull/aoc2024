# read input
with open("input.txt", "r") as f:
    data = f.read()

import re
from itertools import starmap

def mul(a: str, b: str) -> int:
    return int(a) * int(b)

# part 1
pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
part1 = sum(starmap(mul, pattern.findall(data)))
print(f"part1 = {part1}")

# part 2
pattern2 = re.compile(r"don't\(\).+?do\(\)", re.S)
pattern3 = re.compile(r"don't\(\).+", re.S)
data2 = pattern3.sub("", pattern2.sub("", data))
part2 = sum(starmap(mul, pattern.findall(data2)))
print(f"part2 = {part2}")
