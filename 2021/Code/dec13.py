import os

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n\n')
        file.close()
    coordinates = [[int(a) for a in x.split(',')] for x in lines[0].split('\n')]
    fold = [x.split()[2] for x in lines[1].split('\n')]
    return coordinates, fold

def get_matrix(lines):
    width = max([int(line[0]) for line in lines])+1
    height = max([int(line[1]) for line in lines])+1
    matrix = [['.' for _ in range(width)] for _ in range(height)]
    for x,y in lines:
        matrix[y][x] = '#'
    return matrix

def fold_along_x(matrix):
    new_matrix = [['.' for _ in range(len(matrix[0])//2)] for _ in range(len(matrix))]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])//2):
            if '#' in [matrix[y][x], matrix[y][-x-1]]:
                new_matrix[y][x] = '#'
    return new_matrix

def fold_along_y(matrix):
    new_matrix = [['.' for _ in range(len(matrix[0]))] for _ in range(len(matrix)//2)]
    for y in range(len(matrix)//2):
        for x in range(len(matrix[0])):
            if '#' in [matrix[y][x], matrix[-y-1][x]]:
                new_matrix[y][x] = '#'
    return new_matrix

# Part 1
def part1(filepath):
    coordinates, fold = read_file(filepath)
    matrix = get_matrix(coordinates)
    if 'x' in fold[0]:
        matrix = fold_along_x(matrix)
    elif 'y' in fold[0]:
        matrix = fold_along_y(matrix)
    count = 0
    for row in matrix:
        count += row.count('#')
    print(count)


# Part 2
def part2(filepath):
    coordinates, fold = read_file(filepath)
    matrix = get_matrix(coordinates)

    for instruction in fold:
        if 'x' in instruction:
            matrix = fold_along_x(matrix)
        elif 'y' in instruction:
            matrix = fold_along_y(matrix)

    for row in matrix:
        print(''.join(row))

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec13_test.txt'
    filename = 'dec13.txt'
    filepath = os.path.join(path, filename)
    #part1(filepath)
    part2(filepath)
    pass