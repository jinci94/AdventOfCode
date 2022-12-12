import os

"""
The code is a bit slow, but the answer is around 350.

The running time is around 1 min
(57 sec for part 1 and 8 sec for part 2)
"""

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    return lines

class Map:  # for part 1
    def __init__(self, map):
        self.map = map
        self.end = self.find_end()
        self.visited = []
        self.to_visit_now = [self.find_start()]
        self.rows = len(self.map)
        self.columns = len(self.map[0])
        self.elevations = 'SabcdefghijklmnopqrstuvwxyzE'
        self.count_steps = 0

    def find_start(self):
        for i, row in enumerate(self.map):
            for j, pos in enumerate(row):
                if pos == 'S':
                    return (i,j)
    
    def find_end(self):
        for i, row in enumerate(self.map):
            for j, pos in enumerate(row):
                if pos == 'E':
                    return (i,j)
    
    def walk(self):
        to_visit_next = []
        for (i,j) in self.to_visit_now:
            temp_positions = [(max(0,i-1), j), (min(self.rows-1,i+1), j), (i, max(0,j-1)), (i, min(self.columns-1, j+1))]
            for pos in temp_positions:
                if (pos not in self.visited + self.to_visit_now + to_visit_next and 
                    self.map[pos[0]][pos[1]] in self.elevations[:self.elevations.index(self.map[i][j])+2]):
                    to_visit_next.append(pos)
        self.to_visit_now = to_visit_next
        self.count_steps += 1

    def run(self):
        while self.end not in self.to_visit_now:
            self.walk()
            if self.count_steps%100 == 0:
                print('.')
        print(self.count_steps)

class ReversedMap:  # for part 2
    def __init__(self, map):
        self.map = map
        self.start = self.find_start()
        self.visited = []
        self.to_visit_now = [self.find_end()]
        self.rows = len(self.map)
        self.columns = len(self.map[0])
        self.elevations = 'SabcdefghijklmnopqrstuvwxyzE'
        self.count_steps = 0

    def find_start(self):
        start_positions = []
        for i, row in enumerate(self.map):
            for j, pos in enumerate(row):
                if pos == 'S' or pos == 'a':
                    start_positions.append((i,j))
        return start_positions
    
    def find_end(self):
        for i, row in enumerate(self.map):
            for j, pos in enumerate(row):
                if pos == 'E':
                    return (i,j)
    
    def walk(self):
        to_visit_next = []
        for (i,j) in self.to_visit_now:
            temp_positions = [(max(0,i-1), j), (min(self.rows-1,i+1), j), (i, max(0,j-1)), (i, min(self.columns-1, j+1))]
            for pos in temp_positions:
                if (pos not in self.visited + self.to_visit_now + to_visit_next and 
                    self.map[pos[0]][pos[1]] in self.elevations[self.elevations.index(self.map[i][j])-1:]):
                    to_visit_next.append(pos)
        self.to_visit_now = to_visit_next
        self.count_steps += 1

    def run(self):
        while not any([start in self.to_visit_now for start in self.start]):
            self.walk()
            if self.count_steps%100 == 0:
                print('.')
        print(self.count_steps)


# Part 1
def part1(lines):
    mapObj = Map(lines)
    mapObj.run()

# Part 2
def part2(lines):
    mapObj = ReversedMap(lines)
    mapObj.run()

if __name__ == "__main__":
    test = True
    test = False
    if test:
        path = os.path.dirname(os.path.abspath('AoC'))
        filename = "test.txt"
    else:
        path = os.path.dirname(os.path.abspath(__file__))
        filename = "2022_dec12.txt"
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)