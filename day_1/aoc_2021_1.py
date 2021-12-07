# Return input data as list of integers
def get_data(filename):
    return [int(a) for a in open(filename).readlines()]


# Count the number of times the depth increases
def count_increments(depths):
    return sum((1 if b > a else 0) for a, b in zip(depths, depths[1:]))


# Calculate the 3-member sliding window list
def sliding_window(depths):
    return [sum([a, b, c]) for a, b, c in zip(depths, depths[1:], depths[2:])]


def main():
    filename = 'input.txt'
    data = get_data(filename)

    solution_1 = count_increments(data)
    solution_2 = count_increments(sliding_window(data))
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
