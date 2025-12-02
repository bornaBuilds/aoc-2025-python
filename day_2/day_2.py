# Day 2: Gift Shop


def parse_ranges(filename):
    with open(filename) as file:
        line = file.readline().strip()
        ranges = [tuple(map(int, r.split("-"))) for r in line.split(",") if r]
    return ranges


# Part 1: exactly two repeats
def is_repeated_sequence(num):
    number_string = str(num)
    if len(number_string) % 2 != 0:
        return False
    half = len(number_string) // 2
    if number_string[:half] == number_string[half:] and number_string[0] != "0":
        return True
    return False


# Part 2: at least two repeats
def is_repeated_at_least_twice(num):
    number_string = str(num)
    n = len(number_string)
    if n < 2 or number_string[0] == "0":
        return False
    for size in range(1, n // 2 + 1):
        if n % size != 0:
            continue
        chunk = number_string[:size]
        if chunk * (n // size) == number_string:
            return True
    return False


def part_1(ranges):
    invalid = []
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_repeated_sequence(num):
                invalid.append(num)
    return invalid


def part_2(ranges):
    invalid = []
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_repeated_at_least_twice(num):
                invalid.append(num)
    return invalid


ranges = parse_ranges("input.txt")
print("Part 1 answer:", sum(part_1(ranges)))
print("Part 2 answer:", sum(part_2(ranges)))
