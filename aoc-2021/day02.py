with open("input/day02.txt") as f:
    data = [x.strip() for x in f.readlines()]


def part1():
    depth = horizontal = 0
    for i in data:
        x = int(i.split()[1])
        if i.startswith("forward"):
            horizontal += x
        else:
            depth += x if i.startswith("down") else -x
    return depth * horizontal


def part2():
    depth = horizontal = aim = 0
    for i in data:
        x = int(i.split()[1])
        if i.startswith("forward"):
            horizontal += x
            depth += aim * x
        else:
            aim += x if i.startswith("down") else -x
    return depth * horizontal
