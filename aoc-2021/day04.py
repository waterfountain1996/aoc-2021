class Board:

    def __init__(self, numbers: list[list[int]]):
        self._nums = numbers
        self._marked = set()

    def mark(self, num: int):
        if not (pos := self._find(num)):
            return

        self._marked.add(pos)

    def _find(self, num: int):
        for i, r in enumerate(self._nums):
            for j, c in enumerate(r):
                if c == num:
                    return (i, j)

    @property
    def sum_unmarked(self):
        return sum(
            x for i, y in enumerate(self._nums)
            for j, x in enumerate(y)
            if (i, j) not in self._marked
        )

    @property
    def has_won(self):
        for i in range(5):
            row = len({x for x in self._marked if x[0] == i})
            col = len({x for x in self._marked if x[1] == i})
            if col == 5 or row == 5:
                return True
        return False


def parse(input: str):
    head, *rest = input.split("\n\n")
    nums = [int(n) for n in head.split(",")]
    boards = {
        Board(
            [[int(x) for x in row.split()] for row in x.strip().split("\n")]
        )
        for x in rest
    }
    return nums, boards


nums, boards = parse(open("input/day04.txt").read())


def part1():
    for num in nums:
        for board in boards:
            board.mark(num)
            if board.has_won:
                return board.sum_unmarked * num


def part2():
    has_won = set()
    for num in nums:
        global boards
        boards = boards ^ has_won
        has_won.clear()

        for board in boards:
            board.mark(num)
            if board.has_won:
                if len(boards) == 1:
                    return boards.pop().sum_unmarked * num
                has_won.add(board)
