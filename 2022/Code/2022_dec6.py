from inspect import stack
from itertools import count
import os

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        line = file.read().strip()
        file.close()
    return line

# Part 1
def part1(lines):
    for i in range(len(lines)-3):
        if len(list(set(lines[i:i+4]))) == 4:
            return i+4

# Part 2
def part2(lines):
    for i in range(len(lines)-13):
        if len(list(set(lines[i:i+14]))) == 14:
            return i+14

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = "test.txt"
    filename = "2022_dec6.txt"
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    print(part1(lines))
    print(part2(lines))