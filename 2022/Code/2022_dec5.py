from inspect import stack
from itertools import count
import os

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().split('\n\n')
        file.close()
    return lines

# Part 1
def part1(lines):
    temp_stackes, temp_steps = lines
    temp_stackes = temp_stackes.split('\n')
    stackes = [[] for _ in range(int(temp_stackes[-1].strip().split()[-1]))]
    for i in range(len(temp_stackes)-1):
        for j in range(1,len(temp_stackes[-1]), 4):
            if temp_stackes[i][j] != ' ':
                stackes[(j-1)//4].append(temp_stackes[i][j])
    
    steps = [[int(x) for x in line.split()[1::2]] for line in temp_steps.split('\n')]
    for step in steps:
        for _ in range(step[0]):
            stackes[step[2]-1].insert(0, stackes[step[1]-1].pop(0))

    end = ''
    for i in range(len(stackes)):
        end += stackes[i].pop(0)
    print(end)


# Part 2
def part2(lines):
    temp_stackes, temp_steps = lines
    temp_stackes = temp_stackes.split('\n')
    stackes = [[] for _ in range(int(temp_stackes[-1].strip().split()[-1]))]
    for i in range(len(temp_stackes)-1):
        for j in range(1,len(temp_stackes[-1]), 4):
            if temp_stackes[i][j] != ' ':
                stackes[(j-1)//4].append(temp_stackes[i][j])
    
    steps = [[int(x) for x in line.split()[1::2]] for line in temp_steps.split('\n')]
    for step in steps:
        for i in range(step[0]):
            stackes[step[2]-1].insert(i, stackes[step[1]-1].pop(0))

    end = ''
    for i in range(len(stackes)):
        end += stackes[i].pop(0)
    print(end)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = "test.txt"
    filename = "2022_dec5.txt"
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)