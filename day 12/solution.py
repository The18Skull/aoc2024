# read input
with open("input.txt", "r") as f:
    data = f.read().strip()

garden: list[list[str]] = []
for line in data.splitlines():
    garden.append(list(line))

class Map:
    def __init__(self, _map: list[list[str]]) -> None:
        self._map = _map

    def copy(self) -> "Map":
        data = [x.copy() for x in self._map]
        return Map(data)

    def get(self, x: int, y: int) -> str:
        w, h = self.size()
        if x < 0 or x >= w or y < 0 or y >= h:
            return "$"
        return self._map[y][x]

    def set(self, x: int, y: int, val: str) -> None:
        self._map[y][x] = val

    def size(self) -> tuple[int, int]:
        return len(self._map[0]), len(self._map)

new_map = Map(garden)

# gui
from itertools import product
import tkinter as tk
from typing import Any

BLOCK_SIZE = 7 if len(data) > 200 else 21
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
CORNERS = list(zip(DIRECTIONS, (DIRECTIONS * 2)[1:5]))

def flood_fill(data: Map, x: int, y: int, buffer: set[tuple[int, int]] | None = None) -> set[tuple[int, int]] | None:
    buf = buffer if buffer is not None else set()
    buf.add((x, y))

    val = data.get(x, y)
    for (dx, dy) in DIRECTIONS:
        nx = x + dx; ny = y + dy
        if (nx, ny) not in buf and val == data.get(nx, ny):
            flood_fill(data, nx, ny, buf)

    if buffer is not None:
        return
    return buf

class App(tk.Tk):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._width, self._height = new_map.size()

        sizes = list(range(0, 255, 64))[:-1] + [255]
        self._colors = {
            chr(ord("A") + i): "#%02x%02x%02x" % x
            for i, x in enumerate(product(sizes, repeat=3))
            if i < 26
        }

        super().__init__(*args, **kwargs)
        self.title("AoC 2024 - Day 12")
        w = self._width * BLOCK_SIZE
        h = self._height * BLOCK_SIZE
        self.geometry(f"{w}x{h + 50}")
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, width=w, height=h)
        self.canvas.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        frame = tk.Frame(self)
        tk.Button(frame, text="Part 1", command=self.part1).pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        tk.Button(frame, text="Part 2", command=self.part2).pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        frame.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        self.render(new_map)

    # redraw cells
    def render(self, data: Map) -> None:
        w = self._width * BLOCK_SIZE
        h = self._height * BLOCK_SIZE
        self.canvas.create_rectangle(0, 0, w, h, fill="white")

        for j in range(self._width):
            for i in range(self._height):
                v = data.get(j, i)
                c = self._colors.get(v, (255, 255, 255))
                x, y = j * BLOCK_SIZE, i * BLOCK_SIZE
                self.canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill=c)

    def find_regions(self, data: Map) -> list[tuple[int, int]]:
        new_map = data.copy()

        res = []
        for j in range(self._width):
            for i in range(self._height):
                val = new_map.get(j, i)
                if val == "$":
                    continue

                cells = flood_fill(new_map, j, i)
                for (x, y) in cells:
                    new_map.set(x, y, "$")
                res.append(cells)
        return res

    # part 1
    def part1(self) -> None:
        regions = self.find_regions(new_map)

        part1 = 0
        for cells in regions:
            edges = [
                e for (x, y) in cells
                if (e := len([
                    (x + dx, y + dy) for (dx, dy) in DIRECTIONS
                    if new_map.get(x, y) != new_map.get(x + dx, y + dy)
                ]))
            ]
            part1 += len(cells) * sum(edges)
        print(f"part1 = {part1}")

    # part 2
    def part2(self) -> None:
        regions = self.find_regions(new_map)

        part2 = 0
        for cells in regions:
            corners = []
            for (x, y) in cells:
                val = new_map.get(x, y)
                for (d1, d2) in CORNERS:
                    dx1, dy1 = x + d1[0], y + d1[1]
                    dx2, dy2 = x + d2[0], y + d2[1]
                    dx3, dy3 = dx1 + d2[0], dy1 + d2[1]
                    if new_map.get(dx1, dy1) != val and new_map.get(dx2, dy2) != val or \
                        new_map.get(dx1, dy1) == val and new_map.get(dx2, dy2) == val and new_map.get(dx3, dy3) != val:
                        corners.append((x, y))
            part2 += len(cells) * len(corners)
        print(f"part2 = {part2}")

App().mainloop()
