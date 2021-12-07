# Return input data as list of strings
def get_data(filename):
    return [str(a) for a in open(filename).read().splitlines()]


def main():
    filename = 'input.txt'
    data = get_data(filename)

    solution_1 = 0
    solution_2 = 0
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
