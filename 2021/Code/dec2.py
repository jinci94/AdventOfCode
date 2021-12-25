import os

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    return lines

# Part 1
def part1(lines):
    count = {'forward':0, 'down':0, 'up':0}
    for line in lines:
        direction, steps = line.split()
        count[direction] += int(steps)
    print((count['down']-count['up'])*count['forward'])

# Part 2
def part2(lines):
    count = {'forward':0, 'down':0, 'aim':0}
    for line in lines:
        direction, steps = line.split()
        if direction == 'down':
            count['aim'] += int(steps)
        elif direction == 'up':
            count['aim'] -= int(steps)
        else:   # forward
            count['forward'] += int(steps)
            count['down'] += count['aim']*int(steps)
    print(count['down']*count['forward'])

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec2.txt'
    filename = os.path.join(path, filename)
    lines = read_file(filename)
    part1(lines)
    part2(lines)
    pass