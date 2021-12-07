# Return input data as list of strings
def get_data(filename):
    return [str(a) for a in open(filename).read().splitlines()]


def main():
    # Get input data
    filename = 'input.txt'
    data = get_data(filename)

    # Day 1.1
    solution_1 = 0
    # Day 1.2
    solution_2 = 0
    # Report solution
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
