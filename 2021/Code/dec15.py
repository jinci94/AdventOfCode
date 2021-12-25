import os

class MAP_BFS:
    def __init__(self, map_matrix, start, end, size):
        self.map_matrix = map_matrix
        self.count_matrix = [[None for _ in range(len(map_matrix[0]))] for _ in range(len(map_matrix))]
        self.start = start
        self.end = end
        self.size = size
        self.queue = [start]

    def count(self, this):
        # possibility to walk in that direction (True/False)
        up = this[0] > 0
        down = this[0] < self.size[0]-1
        left = this[1] > 0
        right = this[1] < self.size[1]-1
        # coordinates to the next direction
        N = (this[0]-1, this[1])
        S = (this[0]+1, this[1])
        W = (this[0], this[1]-1)
        E = (this[0], this[1]+1)

        for condition, coord in zip([up, down, left, right], [N, S, W, E]):
            if condition:
                this_path = self.count_matrix[this[0]][this[1]] + self.map_matrix[coord[0]][coord[1]]
                if self.count_matrix[coord[0]][coord[1]] == None or self.count_matrix[coord[0]][coord[1]] > this_path:
                    self.count_matrix[coord[0]][coord[1]] = this_path
                    self.queue.append(coord)

    def walk(self):
        self.count_matrix[0][0] = 0
        while self.queue:
            next = self.queue.pop(0)
            self.count(next)
        print(self.count_matrix[-1][-1])



def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    matrix = [[int(x) for x in line] for line in lines]
    return matrix

# Part 1
def part1(matrix):
    size = len(matrix)
    map_matrix = MAP_BFS(matrix, (0,0), (size-1, size-1), (size,size))
    map_matrix.walk()

# Part 2
def bigger(matrix, n):
    size = len(matrix)
    new_matrix = [[0 for _ in range(len(matrix[0])*n)] for _ in range(len(matrix)*n)]
    for j in range(n):
        for i in range(n):
            for r,row in enumerate(matrix):
                for c,col in enumerate(row):
                    new_matrix[r + size*i][c + size*j] = (col+i+j-1)%9+1
    return new_matrix

def part2(matrix):
    matrix = bigger(matrix, 5)
    size = len(matrix)
    map_matrix = MAP_BFS(matrix, (0,0), (size-1, size-1), (size,size))
    map_matrix.walk()

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec15_test.txt' # part1: 0.00166 , part2: 0.01232
    filename = 'dec15.txt'      # part1: 0.12475 , part2: 9.36459
    filepath = os.path.join(path, filename)
    matrix = read_file(filepath)
    part1(matrix)
    part2(matrix)
