from collections import Counter
from itertools import pairwise

def parse(input: str):
    template, pairs = input.split("\n\n")
    pairs = [tuple(p.split(" -> ")) for p in pairs.splitlines(False)]
    pairs = {k: v for k, v in pairs}
    return template, pairs


template, pairs = parse(open("input/day14.txt").read().strip())


def fast_insert(template: str, pairs: dict[str, str], steps: int = 1):
    cc = Counter("".join(p) for p in pairwise(template))

    for _ in range(steps):
        updated = Counter()

        for p in cc:
            n = cc[p]
            if n > 0:
                ins = pairs.get(p)
                p1, p2 = f"{p[0]}{ins}", f"{ins}{p[1]}"

                # Remove the pair from the counter as it was split.
                cc[p] = 0

                # Update the counters for both new pairs.
                updated.update({p1: n, p2: n})

        cc.update(updated)
    return cc


def solve(template, pairs, steps):
    polymer = fast_insert(template, pairs, steps)
    elements = set("".join(polymer.keys()))
    cc = Counter(
        {k: sum(v for x, v in polymer.items() if x[1] == k) for k in elements}
    ).most_common()
    return cc[0][1] - cc[-1][1]


def part1(steps = 10):
    return solve(template, pairs, steps)


def part2(steps = 40):
    return solve(template, pairs, steps)
