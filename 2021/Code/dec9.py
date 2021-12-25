import os

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    return lines

# Part 1
def part1(lines):
    coordinates = []
    lines = [[99] + [int(y) for y in x] + [99] for x in lines]
    lines = [[99 for _ in range(len(lines[0]))]]+ \
             [row for row in lines] +\
             [[99 for _ in range(len(lines[0]))]]
    count = 0
    for i,row in enumerate(lines[1:-1], start=1):
        for j, col in enumerate(row[1:-1], start=1):
            if all([col < x for x in [lines[i-1][j], lines[i+1][j], lines[i][j-1], lines[i][j+1]]]):
                count += col + 1
                coordinates.append((i,j))
    print(count)
    return coordinates, lines


# Part 2
class Map:
    def __init__(self, coordinates, matrix):
        self.coordinates = coordinates
        self.matrix = matrix
        self.max_length = len(self.matrix[0])-1
        self.max_hight = len(self.matrix)-1
        self.basin = [0,0,0]
        self.temp_count = 0

    def _basin(self, x,y):
        if self.matrix[x][y] < 9:
            self.temp_count += 1
            self.matrix[x][y] = 9
            self._basin(min(x+1, self.max_hight),y)
            self._basin(max(x-1, 0),y)
            self._basin(x,min(y+1, self.max_length))
            self._basin(x,max(y-1, 0))
        return self.temp_count

    def find_basins(self):
        for x,y in self.coordinates:
            self.temp_count = 0
            count = self._basin(x,y)
            if any([count > basin for basin in self.basin]):
                lowest_basin = min(self.basin)
                i = self.basin.index(lowest_basin)
                self.basin[i] = count
        print(self.basin[0]*self.basin[1]*self.basin[2])




def part2(lines):
    coordinates, matrix = part1(lines)
    map = Map(coordinates, matrix)
    map.find_basins()
    

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec9_test.txt'
    filename = 'dec9.txt'
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    #part1(lines)
    part2(lines)
    