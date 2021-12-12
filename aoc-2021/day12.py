from collections import Counter


def parse(input: list[str]):
    data = [line.split("-") for line in input]
    caves = {}
    for start, end in data:
        if start not in caves:
            caves[start] = set()

        if end not in caves:
            caves[end] = set()

        caves[start].add(end)
        caves[end].add(start)

    caves = {k: (v - set(["start"])) for k, v in caves.items() if k != "end"}
    return caves


caves = parse([x.strip() for x in open("input/day12.txt").readlines()])


def dfs(start: str, ignore: set):
    if start == "end":
        return 1

    seen = ignore.copy()
    if start.islower():
        seen.add(start)

    return sum(dfs(c, seen) for c in caves[start] if c not in seen)


def dfs2(start: str, ignore: Counter):
    if start == "end":
        return 1

    seen = ignore.copy()
    if start.islower():
        if start not in seen:
            seen[start] = 0

        seen[start] += 1

    # If we've hit any small cave twice, just filter visited caves.
    if any(seen[x] > 1 for x in seen):
        further = [c for c in caves[start] if c not in seen]
    # Otherwise do not filter.
    else:
        further = [c for c in caves[start]]

    return sum(dfs2(c, seen) for c in further)


def part1():
    return dfs("start", set())


def part2():
    return dfs2("start", Counter())
