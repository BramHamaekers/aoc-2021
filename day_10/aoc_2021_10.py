# Return input data as list of strings
from numpy import median


def get_data(filename):
    return [str(a) for a in open(filename).readlines()]


def opposite(string):
    match string:
        case ']': return '['
        case ')': return '('
        case '}': return '{'
        case '>': return '<'
        case _: return None


def find_errors_and_missing(data):
    missing = []
    errors = []
    for line in data:
        illegal = False
        order = []
        for char in line:
            opp = opposite(char)
            if not opp:
                order.append(char)      # char = opening character
            else:                       # char = closing character
                if order[-1] == opp:
                    order.pop(-1)
                else:
                    illegal = True; errors.append(char); break
        if not illegal: missing.append(order)
    return errors, missing


def find_scores(data):
    errors, missing = find_errors_and_missing(data)
    illegal_score, scores = 0, []
    for char in errors:
        match char:
            case ')': illegal_score += 3
            case ']': illegal_score += 57
            case '}': illegal_score += 1197
            case '>': illegal_score += 25137
    for line in missing:
        score = 0
        for char in line[::-1]:
            score *= 5
            match char:
                case '(': score += 1
                case '[': score += 2
                case '{': score += 3
                case '<': score += 4
        scores.append(score)
    return illegal_score, round(median(scores))


def main():
    filename = 'input.txt'
    data = get_data(filename)

    solution_1 = find_scores(data)[0]
    solution_2 = find_scores(data)[1]
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
