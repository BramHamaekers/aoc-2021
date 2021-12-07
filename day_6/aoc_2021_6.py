from collections import Counter


class School:
    def __init__(self, data: list[int]):
        self.fish = Counter(data)

    # Update the school 1 day
    def update(self):
        self.fish = {k-1: v for k, v in self.fish.items()}
        self.fish[8] = self.fish.pop(-1, 0)
        if 6 in self.fish: self.fish[6] += self.fish[8]
        else: self.fish[6] = self.fish[8]


# Return input data as list of strings
def get_data(filename):
    return [int(a) for a in open(filename).read().split(',')]


# return the amount of fish after a certain amount of days
def count_fish(data, days):
    school = School(data)
    for _ in range(days):
        school.update()
    return sum(school.fish.values())


def main():
    # Get input data
    filename = 'input.txt'
    data = get_data(filename)

    # Day 1.1
    solution_1 = count_fish(data, 80)
    # Day 1.2
    solution_2 = count_fish(data, 256)
    # Report solution
    print(f'solution 1: {solution_1}\nsolution 2: {solution_2}')


if __name__ == '__main__':
    main()
