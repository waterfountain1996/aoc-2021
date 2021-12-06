from collections import deque


data = [int(x) for x in open("input/day06.txt").read().strip().split(",")]


def creates_at(fish, lifetime):
    if fish >= lifetime:
        return []

    lifetime -= fish
    if not lifetime:
        return [fish + 1]

    gens = [fish + 1]
    while lifetime > 7:
        gens.append(gens[-1] + 7)
        lifetime -= 7
    return gens


def total_fish(fish, lifetime):
    gens = creates_at(fish, lifetime)
    if not gens:
        return 0

    total = len(gens)
    for g in gens:
        total += total_fish(8, lifetime-g)

    return total


def part1(lifetime = 18):
    # Brute force
    # for _ in range(80):
    #     global data
    #     data = [x - 1 for x in data]
    #     for i, x in enumerate(data):
    #         if x < 0:
    #             data[i] = 6
    #             data.append(8)
    # return len(data)

    # Little faster, still not good enough for part 2
    return sum(total_fish(fish, lifetime) for fish in data) + len(data)


def part2(lifetime = 256):
    total = len(data)

    expected = [data.count(i) for i in range(9)]
    dq = deque(expected)
    for _ in range(lifetime):
        n = dq.popleft()
        total += n
        dq.append(n if n else 0)
        dq[6] = dq[6] + n
        
    return total
