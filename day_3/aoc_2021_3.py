import numpy as np


# Return input data as list of arrays for each binary number in input
def get_data(filename):
    return [np.fromiter(a, dtype=int) for a in open(filename).read().splitlines()]


# convert list to binary number
def list_to_bin(lst):
    return ''.join(str(i) for i in lst)


# Get gamma value from list of numpy arrays
def get_gamma(matrix):
    _, n = matrix.shape
    gamma = list()
    for array in matrix:
        nz = np.count_nonzero(array)
        gamma.append(1) if (nz >= n / 2) else gamma.append(0)
    return list_to_bin(gamma)  # convert list to binary number


# Inverts gamma binary string -> Reverse bits: 1 - 0 = 1 / 1 - 1 = 1
def epsilon_from_gamma(gamma):
    return ''.join([str(1 - int(bit)) for bit in gamma])


# Calculate the power consumption given a list of numpy arrays
def power_consumption(matrix):
    gamma = get_gamma(matrix)
    epsilon = epsilon_from_gamma(gamma)
    return int(gamma, 2) * int(epsilon, 2)


# Delete column based on bits in matrix[i]
def delete_column(matrix, i, bit):
    ii = (np.where(matrix[i] != bit)[0])[::-1]
    for jj in ii:
        matrix = np.delete(matrix, jj, 1)
    return matrix


# Get o2 generator rating or co2 scrubber rating from list of numpy arrays
def life_support_metric(matrix, o2=True):
    a, b = (1, 0) if o2 else (0, 1)
    m, n = matrix.shape
    for i in range(m):
        nz = np.count_nonzero(matrix[i])
        matrix = delete_column(matrix, i, a) if (nz >= n / 2) else delete_column(matrix, i, b)
        _, n = matrix.shape
        if n == 1: break
    return list_to_bin(np.transpose(matrix).flatten())


# Calculate the life support rating given a list of numpy arrays
def life_support(matrix):
    o2 = life_support_metric(matrix, o2=True)
    co2 = life_support_metric(matrix, o2=False)
    return int(o2, 2) * int(co2, 2)


def main():
    # Get input data
    filename = 'input.txt'
    data = get_data(filename)
    matrix = np.column_stack(data)  # create rows of first bits

    # Day 1.1
    solution_1 = power_consumption(matrix)
    # Day 1.2
    solution_2 = life_support(matrix)
    # Report solution
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
