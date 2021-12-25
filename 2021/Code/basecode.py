import os

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    return lines

# Part 1
def part1(lines):
    pass

# Part 2
def part2(lines):
    pass

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'test.txt'
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    #part2(lines)
    pass