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
    for i in range(len(lines)-1):
        if int(lines[i]) < int(lines[i+1]):
            count += 1
    print(count)

# Part 2
def part2(lines):
    count = 0
    for i in range(len(lines)-3):
        if int(lines[i])+int(lines[i+1])+int(lines[i+2]) < int(lines[i+1])+int(lines[i+2])+int(lines[i+3]):
            count += 1
    print(count)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = "dec1.txt"
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)
