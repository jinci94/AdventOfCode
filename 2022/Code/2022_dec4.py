from itertools import count
import os

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split()
        file.close()
    return lines

# Part 1
def part1(lines):
    count = 0
    for line in lines:
        pairs = line.split(',')
        first = pairs[0].split('-')
        second = pairs[1].split('-')
        if (( int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]) ) or
           ( int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]) )):
            count += 1
    print(count)

# Part 2
def part2(lines):
    count = 0
    for line in lines:
        count += 1
        pairs = line.split(',')
        first = pairs[0].split('-')
        second = pairs[1].split('-')
        if (int(first[1]) < int(second[0])  or
            int(first[0]) > int(second[1])):
            count -= 1
    print(count)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = "test.txt"
    filename = "2022_dec4.txt"
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)