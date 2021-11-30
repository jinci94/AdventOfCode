
def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split()
        file.close()
    return lines

# Part 1
def part1(filename):
    lines = read_file(filename)
    pass

# Part 2
def part2(filename):
    lines = read_file(filename)
    pass

if __name__ == "__main__":
    #filename = 'test.txt'
    #part1(filename)
    #part2(filename)
    pass