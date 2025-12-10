"""Advent of Code 2025 - Day 1 Solution"""

from utils.helpers import read_lines, read_test_lines

def part1(data: list) -> int:
    zero_count = 0
    lock_pos = 50
    for instruction in data:
        direction = instruction[0]
        amt = int(instruction[1:])
        if direction == "L":
            lock_pos -= amt
        if direction == "R":
            lock_pos += amt
        lock_pos = lock_pos % 100
        if lock_pos == 0:
            zero_count += 1
    return zero_count


def part2(data: list) -> int:
    zero_count = 0
    lock_pos = 50
    for instruction in data:
        direction = instruction[0]
        amt = int(instruction[1:])

        if lock_pos == 0 and direction == "L":
            zero_count -= 1

        zero_count += amt // 100
        amt = amt % 100
        if direction == "L":
            lock_pos -= amt
        if direction == "R":
            lock_pos += amt

        if lock_pos >= 100 or lock_pos <= 0:
            zero_count += 1
        lock_pos = lock_pos % 100
    return zero_count


if __name__ == "__main__":
    data = read_lines(1)
    
    result1 = part1(data)
    print(f"Part 1: {result1}")
    
    result2 = part2(data)
    print(f"Part 2: {result2}")
