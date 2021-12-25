import os

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    return [[int(x) for x in line] for line in lines]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.flashed_coord = []
        self.count_flash = 0
        self.count_temp = 0

    def flashed(self, x, y):
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if ((x+i < len(self.matrix) and x+i >= 0) and
                (y+j < len(self.matrix) and y+j >= 0) and
                self.matrix[x+i][y+j] != 0):
                    if self.matrix[x+i][y+j] == 9:
                        self.matrix[x+i][y+j] = 0
                        self.flashed_coord.append((x+i,y+j))
                        self.count_flash += 1
                        self.count_temp += 1
                    else:
                        self.matrix[x+i][y+j] += 1

    def step1(self):
        self.count_temp = 0
        for i,row in enumerate(self.matrix):
            for j,col in enumerate(row):
                if col == 9:
                    self.matrix[i][j] = 0
                    self.flashed_coord.append((i,j))
                    self.count_flash += 1
                    self.count_temp += 1
                else:
                    self.matrix[i][j] += 1
        while self.flashed_coord:
            x,y = self.flashed_coord.pop(0)
            self.flashed(x,y)
        
        #for row in self.matrix:
        #    print(row)
        #print()
        return self.count_flash, self.count_temp

# Part 1
def part1(matrix):
    matrix = Matrix(matrix)
    for _ in range(100):
        count, _ = matrix.step1()
    print(count)


# Part 2
def part2(matrix):
    size = len(matrix)**2
    matrix = Matrix(matrix)
    count = 0; i = 0
    while count != size:
        _, count = matrix.step1()
        i += 1
    print(i)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec11_test.txt'
    #filename = 'dec11_test2.txt'
    filename = 'dec11.txt'
    filepath = os.path.join(path, filename)
    matrix = read_file(filepath)
    #part1(matrix)
    part2(matrix)
    pass