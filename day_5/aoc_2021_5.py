# class defining a sparse matrix structure
class Sparse:

    def __init__(self):
        self.matrix = {}

    # Given a (x,y) coordinate add the coordinate to the matrix or add 1 to the existing element
    def add_line_element(self, x, y):
        if (x, y) in self.matrix:
            self.matrix[(x, y)] += 1
        else:
            self.matrix[(x, y)] = 1

    # Given x and y return value of (x,y) in sparse matrix
    def get(self, x, y):
        return self.matrix.get(eval("x, y"))

    # Returns amount of overlaps in the diagram
    def count_overlaps(self):
        return len(list(filter(lambda x: x > 1, self.matrix.values())))


# Return input data as list of strings
def get_data(filename):
    return [str(a) for a in open(filename).read().splitlines()]


# Add a horizontal line to the sparse matrix
def add_hor_line(sparse, x, y1, y2):
    if y1 > y2: y1, y2 = y2, y1
    for y in range(y1, y2 + 1): sparse.add_line_element(x, y)


# Add a vertical line to the sparse matrix
def add_vert_line(sparse, x1, x2, y):
    if x1 > x2: x1, x2 = x2, x1
    for x in range(x1, x2 + 1): sparse.add_line_element(x, y)


# Add a diagonal down line to the sparse matrix
def add_diag_down_line(sparse, x1, y1, x2, y2):
    if x1 > x2: x1, y1, x2, y2 = x2, y2, x1, y1
    if x1 - y1 == x2 - y2:
        for i, j in zip(range(x1, x2 + 1), range(y1, y2+1)):
            sparse.add_line_element(i, j)


# Add a diagonal up line to the sparse matrix
def add_diag_up_line(sparse, x1, y1, x2, y2):
    if x2 > x1: x1, y1, x2, y2 = x2, y2, x1, y1
    for i, j in zip(range(x2, x1 + 1)[::-1], range(y1, y2 + 1)):
        sparse.add_line_element(i, j)


# Count the amount of overlaps in the diagram
def count_line_overlaps(data, diag=False):
    sparse = Sparse()
    for line in data:
        [a, b] = line.split(' -> ')
        x1, y1 = int(a[0]), int(a[2])
        x2, y2 = int(b[0]), int(b[2])
        if x1 == x2: add_hor_line(sparse, x1, y1, y2)
        if y1 == y2: add_vert_line(sparse, x1, x2, y1)
        if diag and x1 - y1 == x2 - y2: add_diag_down_line(sparse, x1, y1, x2, y2)
        if diag and x1 + y1 == x2 + y2: add_diag_up_line(sparse, x1, y1, x2, y2)

    return sparse.count_overlaps()


def main():
    # Get input data
    filename = 'test.txt'
    data = get_data(filename)

    # Day 1.1
    solution_1 = count_line_overlaps(data)
    # Day 1.2
    solution_2 = count_line_overlaps(data, diag=True)
    # Report solution
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
