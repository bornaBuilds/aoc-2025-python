# Day 1: Secret Entrance

with open("input.txt", "r") as input:
    puzzle_input_list = input.read().strip().split("\n")

    puzzle_input = []
    for line in puzzle_input_list:
        direction = line[0]
        distance = int(line[1:])
        puzzle_input.append((direction, distance))

safe_dial = list(range(100))
initial_safe_dial_state = 50


def part_1(puzzle_input):

    current_position = initial_safe_dial_state
    occurrences_of_position_at_zero = 0

    for direction, distance in puzzle_input:
        if direction == "R":
            current_position = (current_position + distance) % len(safe_dial)
            # print(current_position, direction, distance)
        elif direction == "L":
            current_position = (current_position - distance) % len(safe_dial)
            # print(current_position, direction, distance)

        if current_position == 0:
            occurrences_of_position_at_zero += 1

    return occurrences_of_position_at_zero


def part_2(puzzle_input):
    current_position = initial_safe_dial_state
    occurrences_of_position_at_zero = 0

    for direction, distance in puzzle_input:
        if direction == "R":
            for step in range(1, distance + 1):
                current_position = (current_position + 1) % len(safe_dial)
                if current_position == 0:
                    occurrences_of_position_at_zero += 1
        elif direction == "L":
            for step in range(1, distance + 1):
                current_position = (current_position - 1) % len(safe_dial)
                if current_position == 0:
                    occurrences_of_position_at_zero += 1

    return occurrences_of_position_at_zero


# Part 1 answer
print("Part 1 answer:", part_1(puzzle_input))

# Part 2 answer
print("Part 2 answer:", part_2(puzzle_input))
