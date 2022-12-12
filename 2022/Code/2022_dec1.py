import os

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split('\n\n')
        lines = [sum([int(x) for x in line.split('\n')]) for line in lines]
        file.close()
    return lines

# Part 1
def part1(lines):
    print(max(lines))

# Part 2
def part2(lines):
    lines.sort()
    print(sum(lines[-3:]))

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = "test.txt"
    filename = "2022_dec1.txt"
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)