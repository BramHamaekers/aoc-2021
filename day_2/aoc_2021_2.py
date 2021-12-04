import math


# Return input data as list of strings
def get_data(filename):
    return [str(a) for a in open(filename).read().splitlines()]


# Return the position of the submarine given a list of commands
def get_position(commands):
    hor, depth = 0, 0
    for command in commands:
        match command.split():
            case "forward", x: hor += int(x)
            case "down", x: depth += int(x)
            case "up", x: depth -= int(x)
    return hor, depth


# Return the position of the submarine given a list of commands (with aim)
def get_position_2(commands):
    hor, depth, aim = 0, 0, 0
    for command in commands:
        match command.split():
            case "forward", x: hor += int(x); depth += aim*int(x)
            case "down", x: aim += int(x)
            case "up", x: aim -= int(x)
    return hor, depth


def main():
    # Get input data
    filename = 'input.txt'
    data = get_data(filename)

    # Day 1.1
    solution_1 = math.prod(get_position(data))
    # Day 1.2
    solution_2 = math.prod(get_position_2(data))
    # Report solution
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
