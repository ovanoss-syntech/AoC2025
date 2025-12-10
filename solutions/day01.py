"""Advent of Code 2025 - Day 1 Solution"""

from utils.helpers import read_lines
from collections.abc import Callable

def rotate(direction: str, amt: int) -> Callable[[int], int]:
    def rotate_right(x: int) -> int:
        return x + amt
    def rotate_left(x: int) -> int:
        return x - amt
    if direction == "R":
        return rotate_right
    if direction == "L":
        return rotate_left

def part1(data: list) -> int:
    zero_count = 0
    lock_pos = 50
    for instruction in data:
        operation = rotate(instruction[0], int(instruction[1:]))
        lock_pos = operation(lock_pos) % 100
        if lock_pos == 0:
            zero_count += 1
    return zero_count


def part2(data: str) -> int:
    """Solve part 2"""
    # TODO: Implement part 2
    return 0


if __name__ == "__main__":
    data = read_lines(1)
    
    result1 = part1(data)
    print(f"Part 1: {result1}")
    
    result2 = part2(data)
    print(f"Part 2: {result2}")
