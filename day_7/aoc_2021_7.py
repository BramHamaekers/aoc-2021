from math import ceil, floor
from statistics import mean, median


# Return input data as list of strings
def get_data(filename):
    return [int(a) for a in open(filename).read().split(',')]


# Calculates the total fuel consumed given a list of crab position if fuel burning is constant rate
def total_fuel_constant(crabs: list[int], position: int):
    return sum(map(lambda x: abs(x-position), crabs))


# Calculates the total fuel consumed given a list of crab position
def total_fuel(crabs: list[int], position: int):
    return sum(map(lambda x: abs(x-position) + sum(range(abs(x-position))), crabs))


# Returns the lowest amount of fuel needed to move into the same position
def lowest_fuel(crabs, constant=True):
    if constant: return total_fuel_constant(crabs, int(median(crabs)))
    return min(total_fuel(crabs, floor(mean(crabs))), total_fuel(crabs, ceil(mean(crabs))))


def main():
    filename = 'input.txt'
    data = get_data(filename)

    solution_1 = lowest_fuel(data)
    solution_2 = lowest_fuel(data, constant=False)
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
