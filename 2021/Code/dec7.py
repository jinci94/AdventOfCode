import os

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = [int(x) for x in file.read().strip().split(',')]
        file.close()
    return lines

# Part 1
def part1(lines):
    least_fuel = 1e10
    maximum = max(lines)
    minimum = min(lines)
    for i in range(minimum, maximum+1):
        tot_fuel = 0
        for crab in lines:
            tot_fuel += abs(crab-i)
        if tot_fuel < least_fuel:
            least_fuel = tot_fuel
    print(least_fuel)

# Part 2
def sum_n(n):
    return n*(n+1)//2

def part2(lines):
    least_fuel = 1e10
    maximum = max(lines)
    minimum = min(lines)
    for i in range(minimum, maximum+1):
        tot_fuel = 0
        for crab in lines:
            tot_fuel += sum_n(abs(crab-i))
        if tot_fuel < least_fuel:
            least_fuel = tot_fuel
    print(least_fuel)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec7_test.txt'
    filename = 'dec7.txt'
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)
    pass