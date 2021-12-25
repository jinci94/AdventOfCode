import os

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    coordinates = [[[int(x) for x in part.split(',')] for part in line.split(' -> ')] for line in lines]  #[[[x11,y11],[x12,y12]], [[x21,y21],[x22,y22]], ...]
    return coordinates

class Lines:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.max = self.calc_maximum()
        self.matrix = [[0 for _ in range(self.max+1)] for _ in range(self.max+1)]

    def calc_maximum(self):
        maximum = 0
        for line in self.coordinates:
            for two_parts in line:
                for part in two_parts:
                    if part > maximum:
                        maximum = part
        return maximum
    
    def get_line(self,line):
        coord = []
        if line[0][0] == line[1][0]:
            for y in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1])+1):
                coord.append((line[0][0], y))
        elif line[0][1] == line[1][1]:
            for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0])+1):
                coord.append((x, line[0][1]))

        # for part 2:
        elif (line[0][1] - line[1][1]) / (line[0][0] - line[1][0]) > 0:
            start, end = (line[0], line[1]) if line[0][0] < line[1][0] else (line[1], line[0])
            y = start[1]
            for x in range(start[0], end[0]+1):
                coord.append((x, y))
                y += 1
        else:
            start, end = (line[0], line[1]) if line[0][0] < line[1][0] else (line[1], line[0])
            y = start[1]
            for x in range(start[0], end[0]+1):
                coord.append((x, y))
                y -= 1
        return coord
    
    def count_danger(self):
        count = 0
        for row in self.matrix:
            for col in row:
                if col >= 2:
                    count += 1
        return count
    
    def run(self):
        for line in self.coordinates:
            coord = self.get_line(line)
            for (x,y) in coord:
                self.matrix[y][x] += 1
        print(self.count_danger())
        

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec5_test.txt'
    filename = 'dec5.txt'
    filepath = os.path.join(path, filename)
    coordinates = read_file(filepath)
    lines = Lines(coordinates)
    lines.run()    

    #for row in lines.matrix:
    #    print(row)
