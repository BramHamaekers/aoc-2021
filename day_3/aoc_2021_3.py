import numpy as np


# Return input data as list of arrays for each binary number in input
def get_data(filename):
    return [np.fromiter(a, dtype=int) for a in open(filename).read().splitlines()]


# convert list to binary number
def list_to_bin(lst):
    return ''.join(str(i) for i in lst)


# Get gamma value from list of numpy arrays
def get_gamma(data):
    matrix = np.column_stack(data)   # create rows of first bits
    _, n = matrix.shape
    gamma = list()
    for array in matrix:
        nz = np.count_nonzero(array)
        if nz >= n/2: gamma.append(1)
        else: gamma.append(0)
    return list_to_bin(gamma)  # convert list to binary number


# Inverts gamma binary string
def epsilon_from_gamma(gamma):
    epsilon = gamma.replace('1', '2')   # replace "1" with "2"
    epsilon = epsilon.replace('0', '1')   # replace "0" with "1"
    epsilon = epsilon.replace('2', '0')   # replace "2" with "0"
    return epsilon


# Calculate the power consumption given a list of numpy arrays
def power_consumption(data):
    gamma = get_gamma(data)
    epsilon = epsilon_from_gamma(gamma)
    return int(gamma, 2) * int(epsilon, 2)


# Delete column based on bits in matrix[i]
def delete_column(matrix, i, bit):
    ii = np.where(matrix[i] != bit)[0]
    jj = ii[::-1]
    for idx in jj:
        matrix = np.delete(matrix, idx, 1)

    return matrix


# Get o2 generator rating from list of numpy arrays
def o2_rating(data):
    matrix = np.column_stack(data)  # create rows of first bits
    m, n = matrix.shape
    for i in range(m):
        nz = np.count_nonzero(matrix[i])
        if nz >= n / 2: matrix = delete_column(matrix, i, 1)
        else: matrix = delete_column(matrix, i, 0)
        _, n = matrix.shape
        if n == 1: break
    return list_to_bin(np.transpose(matrix).flatten())


# Get co2 scrubber rating from list of numpy arrays
def co2_rating(data):
    matrix = np.column_stack(data)  # create rows of first bits
    m, n = matrix.shape
    for i in range(m):
        nz = np.count_nonzero(matrix[i])
        if nz >= n / 2: matrix = delete_column(matrix, i, 0)
        else: matrix = delete_column(matrix, i, 1)
        _, n = matrix.shape
        if n == 1: break
    return list_to_bin(np.transpose(matrix).flatten())


# Calculate the life support rating given a list of numpy arrays
def life_support(data):
    o2 = o2_rating(data)
    co2 = co2_rating(data)
    return int(o2, 2) * int(co2, 2)


def main():
    # Get input data
    filename = 'input.txt'
    data = get_data(filename)

    # Day 1.1
    solution_1 = power_consumption(data)
    # Day 1.2
    solution_2 = life_support(data)
    # Report solution
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
