import os

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split('\n\n')
        file.close()
    order = lines[0].split(',')
    boards = [[line.split() for line in matrix.split('\n')] for matrix in lines[1:]]
    return order, boards

class BINGO:
    def __init__(self, order, boards):
        self.order = order
        self.boards = boards

    def check_bingo(self):
        for i,board in enumerate(self.boards):
            for row in board:
                if all([nr == '#' for nr in row]):
                    return True, i
            for k in range(len(board)):
                if all([board[j][k] == '#' for j in range(len(board))]):
                    return True, i
        return False, None
    
    def count_win(self, i, number):
        count = 0
        for row in self.boards[i]:
            for col in row:
                if col != '#':
                    count += int(col)
        return number*count

    def play(self, number):
        for i,board in enumerate(self.boards):
            for j,row in enumerate(board):
                for k,nr in enumerate(row):
                    if number == nr:
                        self.boards[i][j][k] = '#'
                        bingo, board_nr = self.check_bingo()
                        if bingo:
                            return self.count_win(board_nr, int(number))
        return None

    def run(self):
        for number in self.order:
            val = self.play(number)
            if val != None:
                return val

# Part 1
def part1(filename):
    order, boards = read_file(filename)
    bingo = BINGO(order, boards)
    print(bingo.run())
            
# Part 2
def part2(filename):
    pass

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec4_test1.txt'
    filename = 'dec4.txt'
    filename = os.path.join(path, filename)
    part1(filename)
    #part2(filename)
