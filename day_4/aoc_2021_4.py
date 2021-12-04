import pandas as pd


# Return numbers as list and boards as pandas DataFrames
def get_data(filename):
    with open(filename) as file:
        numbers, *boards = file.read().split('\n\n')
        numbers = [int(a) for a in numbers.split(',')]
        boards = [pd.DataFrame(grid) for grid in [[[int(n) for n in line.split()]
                                                   for line in row.split('\n')] for row in boards]]
    return numbers, boards


# Check if a board has won
def check_board(board):
    t = board.transpose()
    row, col = board.eq(board.iloc[:, 0], axis=0).all(1), t.eq(t.iloc[:, 0], axis=0).all(1)
    if col.any() or row.any(): return True


# Return the score of the first winning board
def win_bingo(numbers, boards):
    for numb in numbers:
        for i, board in enumerate(boards):
            boards[i] = board.replace(numb, False)  # False because in df.to_numpy().sum(), True -> 1
            if check_board(boards[i]): return numb * boards[i].to_numpy().sum()
    return 'No solution Found'


# Return the score of the losing board (last winning board)
def lose_bingo(numbers, boards):
    for n, numb in enumerate(numbers):
        for i, board in enumerate(boards):
            boards[i] = board.replace(numb, False)  # False because in df.to_numpy().sum(), True -> 1
            if check_board(boards[i]):
                pop = boards.pop(i)
                if len(boards) == 0: return numb * pop.to_numpy().sum()
                return lose_bingo(numbers[n:], boards)
    return 'No solution Found'


def main():
    # Get input data
    filename = 'input.txt'
    numbers, boards = get_data(filename)

    # Day 1.1
    solution_1 = win_bingo(numbers, boards)
    # Day 1.2
    solution_2 = lose_bingo(numbers, boards)
    # Report solution
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
