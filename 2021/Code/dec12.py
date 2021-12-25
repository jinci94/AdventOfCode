import os

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    return [line.split('-') for line in lines]

class Cave:
    def __init__(self, lines):
        self.path = self.create_dict(lines)
        self.count_ways = 0

    def create_dict(self, lines):
        path = {}
        for a,b in lines:
            if a not in path:
                path[a] = []
            if b not in path:
                path[b] = []
            path[a].append(b)
            path[b].append(a)
        return path

    def _walk(self, a, path):
        for way in self.path[a]:
            if way == 'end':
                self.count_ways += 1
                print(path + ['end'])
            elif way.isupper() or way not in path:
                self._walk(way, path+[a])
    
    def walk(self):
        for way in self.path['start']:
            self._walk(way, ['start'])
        print(self.count_ways)

    def _walk2(self, a, path, visited):
        for way in self.path[a]:
            if way == 'end':
                self.count_ways += 1
            elif way.isupper():
                self._walk2(way, path+[a], visited)
            elif way not in ['start', 'end'] and not visited:
                if way in path:
                    self._walk2(way, path+[a], True)
                else:
                    self._walk2(way, path+[a], False)
            elif way not in path:
                self._walk2(way, path+[a], visited)
    
    def walk2(self):
        for way in self.path['start']:
            self._walk2(way, ['start'], False)
        print(self.count_ways)

    


# Part 1
def part1(lines):
    cave = Cave(lines)
    cave.walk()


# Part 2
def part2(lines):
    cave = Cave(lines)
    cave.walk2()

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec12_test3.txt'
    filename = 'dec12.txt'
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    #part1(lines)
    part2(lines)
    pass