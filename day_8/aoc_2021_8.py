from collections import Counter


def get_data(filename):
    return [str(a) for a in open(filename).read().split('\n')]


def get_input(data):
    return [sorted((elem.split(' | ')[0]).split(' '), key=len) for elem in data]


def get_output(data):
    return [(elem.split(' | ')[1]).split(' ') for elem in data]


# Return amount of output equal to 1,4,7 or 8
# given that len(1) -> 2, len(4) -> 4, len(7) -> 3, len(8) -> 7
def count_unique_output(data):
    output = get_output(data)
    flat_output = [item for sublist in output for item in sublist]
    numbers = [len(x) for x in flat_output]
    count = Counter(numbers)

    return count[2] + count[4] + count[3] + count[7]


def one_four_six(input):
    for elem in input:
        match len(elem):
            case 2: one = tuple(elem)
            case 4: four = tuple(elem)
            case 6:
                if not all(s in elem for s in one): six = tuple(elem)
    return one, four, six


# Convert string output to a number
def calculate_output(input, output):
    one, four, six = one_four_six(input)
    for i, elem in enumerate(output):
        match len(elem):
            case 2: output[i] = 1
            case 4: output[i] = 4
            case 3: output[i] = 7
            case 7: output[i] = 8
            case 6:
                if all(s in elem for s in one):
                    output[i] = 9 if all(s in elem for s in four) else 0
                else: output[i] = 6
            case 5:
                if all(s in elem for s in one): output[i] = 3
                elif all(s in six for s in tuple(elem)): output[i] = 5
                else: output[i] = 2
    return int(''.join(map(str, output)))


def count_all_output(data):
    output = get_output(data)
    input = get_input(data)
    return sum([(calculate_output(i, o)) for i, o in zip(input, output)])


def main():
    filename = 'input.txt'
    data = get_data(filename)

    solution_1 = count_unique_output(data)
    solution_2 = count_all_output(data)
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
