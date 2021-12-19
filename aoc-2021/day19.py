from collections import Counter
from itertools import combinations, product


def parse(input: str):
    scanners = [x.strip() for x in input.split("\n\n")]
    scanners = [[x for x in s.splitlines() if not x.startswith("---")]
                 for s in scanners]
    scanners = [{eval(x) for x in s} for s in scanners]
    return scanners


scanners = parse(open("input/day19.txt").read().strip())


rotations = [
    lambda v: (v[0], v[1], v[2]),
    lambda v: (v[0], -v[1], -v[2]),
    lambda v: (v[0], v[2], -v[1]),
    lambda v: (v[0], -v[2], v[1]),

    lambda v: (v[1], v[0], -v[2]),
    lambda v: (v[1], -v[0], v[2]),
    lambda v: (v[1], v[2], v[0]),
    lambda v: (v[1], -v[2], -v[0]),

    lambda v: (v[2], v[0], v[1]),
    lambda v: (v[2], -v[0], -v[1]),
    lambda v: (v[2], v[1], -v[0]),
    lambda v: (v[2], -v[1], v[0]),

    lambda v: (-v[0], v[1], -v[2]),
    lambda v: (-v[0], -v[1], v[2]),
    lambda v: (-v[0], v[2], v[1]),
    lambda v: (-v[0], -v[2], -v[1]),

    lambda v: (-v[1], v[0], v[2]),
    lambda v: (-v[1], -v[0], -v[2]),
    lambda v: (-v[1], v[2], -v[0]),
    lambda v: (-v[1], -v[2], v[0]),

    lambda v: (-v[2], v[0], -v[1]),
    lambda v: (-v[2], -v[0], v[1]),
    lambda v: (-v[2], v[1], v[0]),
    lambda v: (-v[2], -v[1], -v[0]),
]


def translate(scanner):
    for r in rotations:
        yield [r(p) for p in scanner]


def vectorize(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])


def vadd(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


def solve():
    offsets = {0: (0, 0, 0)}
    rotated = {0}

    while rotated:
        current = rotated.pop()
        s0 = scanners[current]
        for i in range(len(scanners)):
            if i in offsets or i == current:
                continue

            for ps in translate(scanners[i]):
                cc = Counter(vectorize(a, r) for a, r in product(s0, ps))
                if (v := cc.most_common(1)[0])[1] >= 12:
                    scanners[i] = {vadd(p, v[0]) for p in ps}
                    offsets[i] = v[0]
                    rotated.add(i)
                    break
    beacons = {b for s in scanners for b in s}
    dst = max(manhattan(a, b) for a, b in combinations(offsets.values(), 2))
    return len(beacons), dst


def part1():
    return solve()[0]


def part2():
    return solve()[1]
