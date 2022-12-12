import os

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split()
        lines = [line for line in lines]
        file.close()
    return lines

# Part 1
def part1(lines):
    priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    for line in lines:
        x = list(set(line[:len(line)//2]).intersection(set(line[len(line)//2:])))[0]
        count += priority.index(x) + 1
    print(count)


# Part 2
def part2(lines):
    priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    for i in range(0, len(lines), 3):
        x = list(set(lines[i+0]).intersection(set(lines[i+1]), set(lines[i+2])))[0]
        count += priority.index(x) + 1
    print(count)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = "test.txt"
    filename = "2022_dec3.txt"
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)