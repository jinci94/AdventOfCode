import os

# Solves both parts

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n\n')
        file.close()
    scanners = [[tuple([int(x) for x in line.split(',')]) for line in scanner.split('\n')[1:]] for scanner in lines]
    return scanners

class Scanners:
    def __init__(self, scanners):
        self.scanners = scanners
        self.beacon_positions = set(scanners.pop(0))
        self.scanner_positions = set([(0,0,0)])
        self.count = 0; self.total = len(scanners)
        # rotation: the first element inside the tuple is + (1) or - (-1), the second element is x (0), y (1) or z (2)
        self.rotations = [[(1,0), (1,1), (1,2)],   [(1,1), (1,2), (1,0)],   [(1,2), (1,0), (1,1)],
                          [(1,0), (-1,1), (-1,2)], [(1,1), (-1,2), (-1,0)], [(1,2), (-1,0), (-1,1)],
                          [(1,0), (1,2), (-1,1)],  [(1,1), (1,0), (-1,2)],  [(1,2), (1,1), (-1,0)],
                          [(1,0), (-1,2), (1,1)],  [(1,1), (-1,0), (1,2)],  [(1,2), (-1,1), (1,0)],

                          [(-1,0), (1,2), (1,1)],   [(-1,1), (1,0), (1,2)],   [(-1,2), (1,1), (1,0)],
                          [(-1,0), (-1,2), (-1,1)], [(-1,1), (-1,0), (-1,2)], [(-1,2), (-1,1), (-1,0)],
                          [(-1,0), (1,1), (-1,2)],  [(-1,1), (1,2), (-1,0)],  [(-1,2), (1,0), (-1,1)],
                          [(-1,0), (-1,1), (1,2)],  [(-1,1), (-1,2), (1,0)],  [(-1,2), (-1,0), (1,1)]]
        """
        # I used the right-hand-rule to find all rotations for x and -x as the thumb (the first column),
        # then I just rotated the coordinates s.t. x->y->z->x->..., see column 2 and 3.

        rotations = [(x,y,z),    (y,z,x),    (z,x,y),
                    (x,-y,-z),  (y,-z,-x),  (z,-x,-y),
                    (x,z,-y),   (y,x,-z),   (z,y,-x),
                    (x,-z,y),   (y,-x,z),   (z,-y,x),
                    
                    (-x,z,y),   (-y,x,z),   (-z,y,x),
                    (-x,-z,-y), (-y,-x,-z), (-z,-y,-x),
                    (-x,y,-z),  (-y,z,-x),  (-z,x,-y),
                    (-x,-y,z),  (-y,-z,x),  (-z,-x,y)]

        # For the thumb in one direction, we will get 4 rotations around the thumb,
        # and therefor 4 different directions for each "first direction".
        # Ex: thumb in "x"-dir, then rotation around it gives (y,z), (z,-y), (-y,-z), (-z,y)
        # Then we can flip the thumb to the negative direction (-x) and do the same.
        """

    def find_overlap(self, scanner):
        for beacon0 in list(self.beacon_positions):
            for beacon_i in scanner:
                i, j, k = [beacon0[n]-beacon_i[n] for n in range(3)]
                count = 0
                for x,y,z in scanner:
                    if (x+i,y+j,z+k) in self.beacon_positions:
                        count += 1
                if count >= 12:
                    self.count += 1
                    self.scanner_positions.add((i,j,k))
                    print(self.count, self.total)
                    return True, (i,j,k)
        return False, (0,0,0)
    
    def next_scanner(self, scanner):
        for j, rotation in enumerate(self.rotations):
            rotated_scanner = [[rotation[i][0]*beacon[rotation[i][1]] for i in range(3)] for beacon in scanner]
            found, shifting = self.find_overlap(rotated_scanner)
            if found:
                for add_scanner in rotated_scanner:
                    self.beacon_positions.add(tuple([add_scanner[i]+shifting[i] for i in range(3)]))
                return True
        return False
    
    def run(self):
        while self.scanners:
            for i, scanner in enumerate(self.scanners):
                found = self.next_scanner(scanner)
                if found:
                    self.scanners.pop(i)
                    break
        return self.beacon_positions, self.scanner_positions

# Part 1
def part1(scanners):
    beacons, _ = Scanners(scanners).run()
    print(len(beacons))


# Part 2
def manhattan_distance(scanner1, scanner2):
    return sum([abs(scanner1[i]-scanner2[i]) for i in range(3)])

def part2(scanners):
    _, scanners = Scanners(scanners).run()
    scanners = list(scanners)
    count = 0
    for i, scanner1 in enumerate(scanners[:-1]):
        for scanner2 in scanners[i+1:]:
            dist = manhattan_distance(scanner1, scanner2)
            if dist > count:
                count = dist
    print(count)

def both_parts(scanners):
    beacons, scanners = Scanners(scanners).run()
    print('Part 1:', len(beacons))

    scanners = list(scanners)
    count = 0
    for i, scanner1 in enumerate(scanners[:-1]):
        for scanner2 in scanners[i+1:]:
            dist = manhattan_distance(scanner1, scanner2)
            if dist > count:
                count = dist
    print('Part 2:', count)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec19_test.txt'
    filename = 'dec19.txt'
    filepath = os.path.join(path, filename)
    scanners = read_file(filepath)
    #part1(scanners)
    #part2(scanners)
    both_parts(scanners)
