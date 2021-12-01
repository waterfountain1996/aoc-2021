import argparse
import importlib


parser = argparse.ArgumentParser()
parser.add_argument("day", type=int)
parser.add_argument("part", type=int)


def main():
    args = parser.parse_args()
    if not args.day in range(1, 26):
        print("Day must be in range from 1 to 25")
        return

    if not args.part in (1, 2):
        print("Part must be either 1 or 2")
        return

    try:
        md = importlib.import_module(f"day{args.day:02}")
    except ImportError:
        print("No solution... yet")
        return

    try:
        func = getattr(md, f"part{args.part}")
    except AttributeError:
        print("No solution... yet")
    else:
        print(func())


main()
