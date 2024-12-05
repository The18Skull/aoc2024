# read input
with open("input.txt", "r") as f:
    data = f.read()

array = []
for line in data.splitlines():
    arr = list(line)
    array.append(arr)
l = 4

# part 1
words: list[str] = []
for i in range(len(array)):
    for j in range(len(array[i])):
        # horizontal
        if j <= len(array[i]) - l:
            word = ""
            for k in range(l):
                word += array[i][j + k]
            words.append(word)
        # vertical
        if i <= len(array) - l:
            word = ""
            for k in range(l):
                word += array[i + k][j]
            words.append(word)
        # left diagonal
        if i <= len(array) - l and j <= len(array[i]) - l:
            word = ""
            for k in range(l):
                word += array[i + k][j + k]
            words.append(word)
        # right diagonal
        if i <= len(array) - l and j >= l - 1:
            word = ""
            for k in range(l):
                word += array[i + k][j - k]
            words.append(word)
part1 = words.count("XMAS") + words.count("SAMX")
print(f"part1 = {part1}")

# part 2
part2 = 0
for i in range(1, len(array) - 1):
    for j in range(1, len(array[i]) - 1):
        # A is mid
        if array[i][j] != "A":
            continue
        # left diagonal
        if array[i - 1][j - 1] == "M" and array[i + 1][j + 1] == "S" or array[i - 1][j - 1] == "S" and array[i + 1][j + 1] == "M":
            # right diagonal
            if array[i + 1][j - 1] == "M" and array[i - 1][j + 1] == "S" or array[i + 1][j - 1] == "S" and array[i - 1][j + 1] == "M":
                part2 += 1
print(f"part2 = {part2}")
