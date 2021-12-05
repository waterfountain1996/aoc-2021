from collections import Counter


class Line:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def is_horizontal(self):
        return self.x1 == self.x2 or self.y1 == self.y2

    @property
    def points(self):
        px = list(range(min(self.x1, self.x2), max(self.x1, self.x2) + 1))
        if self.x1 > self.x2:
            px.reverse()

        py = list(range(min(self.y1, self.y2), max(self.y1, self.y2) + 1))
        if self.y1 > self.y2:
            py.reverse()

        if len(px) == 1:
            px = px * len(py)
        elif len(py) == 1:
            py = py * len(px)

        return {pp for pp in zip(px, py)}


def parse(input: str):
    points = [n.split("->") for n in input.strip().split("\n")]
    points = [(*p[0].split(","), *p[1].split(",")) for p in points]
    points = [tuple(int(x) for x in p) for p in points]
    lines = [Line(*p) for p in points]
    return lines


data = parse(open("input/day05.txt").read())


def part1():
    lines = [line for line in data if line.is_horizontal]
    cc = Counter(p for line in lines for p in line.points)
    return sum(1 for p in cc if cc[p] > 1)


def part2():
    lines = data
    cc = Counter(p for line in lines for p in line.points)
    return sum(1 for p in cc if cc[p] > 1)
