# Day 3: Lobby

with open("input.txt") as file:
    number_lines = file.read().strip().split("\n")


def find_second_highest_index(sorted_numbers, first_number_index):
    second_number_index = next(
        (i for i in sorted_numbers if i[0] > first_number_index), None
    )
    if second_number_index is None:
        second_number_index = next(
            (i for i in sorted_numbers if i[0] < first_number_index), None
        )

    second_index = second_number_index[0]

    return second_index


def part_1(number_lines):
    joined_highest_numbers_list = []

    for line in number_lines:
        numbers = list(map(int, list(line)))
        sorted_numbers = sorted(enumerate(numbers), key=lambda x: x[1], reverse=True)
        # print(sorted_numbers)
        first_number_index = sorted_numbers[0][0]

        second_index = find_second_highest_index(sorted_numbers, first_number_index)

        indexes_to_join = (
            [first_number_index, second_index]
            if first_number_index < second_index
            else [second_index, first_number_index]
        )
        # print(indexes_to_join)
        joined_highest_numbers_list.append("".join([line[i] for i in indexes_to_join]))

    # print(joined_highest_numbers_list)

    result = sum([int(num) for num in joined_highest_numbers_list])
    return result


part_1_result = part_1(number_lines)
print("Part 1 answer:", part_1_result)
