import math

import numpy as np


def get_data(filename):
    return np.array([[int(b) for b in list(a)] for a in open(filename).read().split('\n')])


def is_local_minima(i, j, data):
    return data[i][j] < data[i-1][j] and data[i][j] < data[i+1][j]\
           and data[i][j] < data[i][j+1] and data[i][j] < data[i][j-1]


def risk_level(data):
    return sum([data[i][j] + 1 for i, j in find_local_minima(data)])


def find_local_minima(data):
    (rows, cols) = data.shape
    minima = []
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if is_local_minima(i, j, data):
                minima.append((i, j))
    return minima


def get_adjacent(i, j, data):
    adjacent = []
    for x, y in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
        if data[x][y] != 9:
            adjacent.append((x, y))
    return adjacent


def find_basin(i, j, data):
    basin = set()
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        if (x, y) not in basin:
            stack += get_adjacent(x, y, data)
            basin.add((x, y))
    return basin


def find_largest_basins(data):
    minima = find_local_minima(data)
    basins = []
    for (i, j) in minima:
        basins.append(len(find_basin(i, j, data)))
    return math.prod(sorted(basins, reverse=True)[:3])



def main():
    filename = 'input.txt'
    data = get_data(filename)
    data = np.pad(data, pad_width=1, mode='constant', constant_values=9)

    solution_1 = risk_level(data)
    solution_2 = find_largest_basins(data)
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
