import os

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split('\n')
        lines = [line.split() for line in lines]
        file.close()
    return lines

def move_T(H, T):
    if abs(H[0]-T[0])<=1 and abs(H[1]-T[1])<=1:
        return T
    elif H[0] == T[0]:
        T0 = T[0]
        T1 = (H[1]+T[1])//2
    elif H[1] == T[1]:
        T0 = (H[0]+T[0])//2
        T1 = T[1]
    elif abs(H[0]-T[0]) == 1:
        T0 = H[0]
        T1 = (H[1]+T[1])//2
    elif abs(H[1]-T[1]) == 1:
        T0 = (H[0]+T[0])//2
        T1 = H[1]
    elif abs(H[0]-T[0]) == 2 and abs(H[1]-T[1]) == 2:
        T0 = (H[0]+T[0])//2
        T1 = (H[1]+T[1])//2

    return (T0, T1)

# Part 1
def part1(lines):
    tail_visited = set()
    H = (0,0); T = (0,0)
    for dir, steps in lines:
        for _ in range(int(steps)):
            if dir == 'R':
                H = (H[0]+1, H[1])
            elif dir == 'L':
                H = (H[0]-1, H[1])
            elif dir == 'U':
                H = (H[0], H[1]+1)
            else:
                H = (H[0], H[1]-1)
            T = move_T(H, T)
            tail_visited.add(T)
    print(len(tail_visited))

# Part 2
def part2(lines):
    tail_visited = set()
    H = [(0,0) for i in range(10)]
    for dir, steps in lines:
        for _ in range(int(steps)):
            if dir == 'R':
                H[0] = (H[0][0]+1, H[0][1])
            elif dir == 'L':
                H[0] = (H[0][0]-1, H[0][1])
            elif dir == 'U':
                H[0] = (H[0][0], H[0][1]+1)
            else:
                H[0] = (H[0][0], H[0][1]-1)
            for i in range(9):
                H[i+1] = move_T(H[i], H[i+1])
            tail_visited.add(H[-1])
    print(len(tail_visited))

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    #path = os.path.dirname(os.path.abspath('AoC'))
    filename = "test.txt"
    filename = "2022_dec9.txt"
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)