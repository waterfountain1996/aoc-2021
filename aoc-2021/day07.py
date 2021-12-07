from math import ceil


data = [int(n) for n in open("input/day07.txt").read().strip().split(",")]
crabs = sorted(data)


def part1():
    median = crabs[len(crabs) // 2]
    return sum(abs(crab - median) for crab in crabs)


def part2():
    # I figured out that the point would be the mean of the set, but
    # it never was a whole number. Ceiling of the mean would give the
    # right answer for the test input, but with the actual input, it
    # would have to be a floored number. I've tested this on multipe
    # inputs and it would not give consistent results, and so thanks
    # to anon from 4chan who said that it would be the minimum sum
    # between floored and rounded number.
    fm = sum(crabs) // len(crabs)
    cm = ceil(sum(crabs) / len(crabs))
    return min(
        sum(sum(range(1, abs(crab - fm) + 1)) for crab in crabs),
        sum(sum(range(1, abs(crab - cm) + 1)) for crab in crabs),
    )
