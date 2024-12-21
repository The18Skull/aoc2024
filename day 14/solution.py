# read input
with open("input.txt", "r") as f:
    data = f.read().strip()

robots: list[tuple[tuple[int, int], tuple[int, int]]] = []
for line in data.splitlines():
    parts = map(lambda x: x[2:], line.split(" ", 1))
    p, v = map(lambda x: list(map(int, x.split(",", 1))), parts)
    robots.append((p, v))

BATHROOM_SIZE = 101, 103

def move(pos: tuple[int, int], vel: tuple[int, int], gen: int) -> tuple[int, int]:
    for _ in range(gen):
        p = []
        for i in range(2):
            o = pos[i] + vel[i]
            if o < 0:
                o = BATHROOM_SIZE[i] + o
            elif o >= BATHROOM_SIZE[i]:
                o -= BATHROOM_SIZE[i]
            p.append(o)
        pos = tuple(p)
    return pos

# gui
import tkinter as tk
from typing import Any

BLOCK_SIZE = 9

class App(tk.Tk):
    def __init__(self, robots: list[tuple[tuple[int, int], tuple[int, int]]], *args: Any, **kwargs: Any) -> None:
        self._robots = robots
        self._width, self._height = BATHROOM_SIZE

        super().__init__(*args, **kwargs)
        self.title("AoC 2024 - Day 14")
        w = self._width * BLOCK_SIZE
        h = self._height * BLOCK_SIZE
        self.geometry(f"{w}x{h + 75}")
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, width=w, height=h)
        self.canvas.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        self._counter = tk.IntVar(self, value=0)

        frame = tk.Frame(self)
        tk.Button(frame, text="Part 1", command=self.part1).pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        tk.Button(frame, text="Part 2", command=self.part2).pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        frame.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
        frame = tk.Frame(self)
        tk.Entry(frame, textvariable=self._counter).pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        tk.Button(frame, text="Simulate", command=self.simulate).pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        frame.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        self.render([x[0] for x in self._robots])

    # show robot's positions
    def render(self, robots: list[tuple[int, int]]) -> None:
        w = self._width * BLOCK_SIZE
        h = self._height * BLOCK_SIZE
        self.canvas.create_rectangle(0, 0, w, h, fill="white")

        mid = BATHROOM_SIZE[0] // 2, BATHROOM_SIZE[1] // 2
        for (j, i) in robots:
            c = "red" if j == mid[0] or i == mid[1] else "green"
            x, y = j * BLOCK_SIZE, i * BLOCK_SIZE
            self.canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill=c)

    def simulate(self) -> None:
        val = self._counter.get()
        positions = list(map(lambda x: move(*x, val), robots))
        self.render(positions)

    # part 1
    def part1(self) -> None:
        mid = BATHROOM_SIZE[0] // 2, BATHROOM_SIZE[1] // 2

        positions = list(map(lambda x: move(*x, 100), robots))
        self.render(positions)

        q1 = len([x for x in positions if x[0] < mid[0] and x[1] < mid[1]])
        q2 = len([x for x in positions if x[0] > mid[0] and x[1] < mid[1]])
        q3 = len([x for x in positions if x[0] < mid[0] and x[1] > mid[1]])
        q4 = len([x for x in positions if x[0] > mid[0] and x[1] > mid[1]])

        part1 = q1 * q2 * q3 * q4
        print(f"part1 = {part1}")

    # part 2
    def part2(self) -> None:
        robots = [(list(p), v) for (p, v) in self._robots]

        part2 = 0
        best = 10000
        for i in range(10000):
            positions = []
            for (p, v) in robots:
                pos = move(p, v, 1)
                positions.append(pos)
                p[0], p[1] = pos

            size = len({x[0] for x in positions}) + len({x[1] for x in positions})
            if size < best:
                best = size
                part2 = i + 1
        print(f"part2 = {part2}")

        self._counter.set(part2)
        self.simulate()

App(robots).mainloop()
