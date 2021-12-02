with open("input/day01.txt") as f:
    data = [int(x) for x in f.read().split()]


def triplewise(iterable):
    if len(iterable) < 3: return

    for i in range(len(iterable)):
        yield iterable[i], iterable[i+1], iterable[i+2]
        if i + 3 == len(iterable):
            break


def part1():
    return sum(1 for i, x in enumerate(data[1:], 1) if data[i-1] < x)


def part2():
    prev = None
    counter = -1
    for triplet in triplewise(data):
        x = sum(triplet)
        if not prev or x > prev:
            counter += 1
        prev = x
    return counter
