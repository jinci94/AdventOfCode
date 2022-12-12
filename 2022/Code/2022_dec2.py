import os

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split('\n')
        lines = [line.split() for line in lines]
        file.close()
    return lines

# Part 1
def part1(lines):
    convert = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
    count = 0
    for line in lines:
        if convert[line[0]] == convert[line[1]]:
            count += 3 + convert[line[1]]
        elif (convert[line[0]]+1)%3 == convert[line[1]]%3:
            count += 6 + convert[line[1]]
        else:
            count += convert[line[1]]
    print(count)
    

# Part 2
def part2(lines):
    convert_result = {'X':0, 'Y':3, 'Z':6} # lose, draw, win
    convert = {'A':1, 'B':2, 'C':3}
    count = 0
    for line in lines:
        count += convert_result[line[1]]
        if line[1] == 'X':      # lose
            if line[0] == 'A':
                count += 3
            else:
                count += convert[line[0]]-1
        elif line[1] == 'Y':    # draw
            count += convert[line[0]]
        else:                   # win
            if line[0] == 'C':
                count += 1
            else:
                count += convert[line[0]]+1
    print(count)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = "test.txt"
    filename = "2022_dec2.txt"
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)