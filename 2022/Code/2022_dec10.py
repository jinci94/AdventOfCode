import os

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    return lines

class CRT:
    def __init__(self):
        self.current_CRT_row = ''
        self.sprite_position = ['.' for _ in range(40)]
        self.image = []
    
    def set_current_CRT_row(self, position):
        self.current_CRT_row += self.sprite_position[position]
        if len(self.current_CRT_row) == 40:
            self.image.append(self.current_CRT_row)
            self.current_CRT_row = ''
        if len(self.image) == 6:
            print('Part 2:')
            for row in self.image:
                print(row)
    
    def set_sprite_position(self, X):
        self.sprite_position = ['#' if pos in [X-1, X, X+1] else '.' for pos in range(40)]


class CPU:
    def __init__(self, instructions):
        self.instructions = instructions
        self.X = 1
        self.clock_circuit = 0
        self.cycles = [20, 60, 100, 140, 180, 220]
        self.signal_strengths = []
        self.crt = CRT()
        self.crt.set_sprite_position(self.X)
    
    def check_signal_strength(self):
        if self.clock_circuit in self.cycles:
            self.signal_strengths.append(self.clock_circuit * self.X)
    
    def run(self):
        for instruction in self.instructions:
            if instruction == 'noop':
                self.crt.set_current_CRT_row(self.clock_circuit%40)
                self.clock_circuit += 1
                self.check_signal_strength()
            else:
                for _ in range(2):
                    self.crt.set_current_CRT_row(self.clock_circuit%40)
                    self.clock_circuit += 1
                    self.check_signal_strength()
                self.X += int(instruction.split()[1])
                self.crt.set_sprite_position(self.X)
        print('\nPart 1:', sum(self.signal_strengths))

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    #path = os.path.dirname(os.path.abspath('AoC'))
    filename = "test.txt"
    filename = "2022_dec10.txt"
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    # Part 1 and 2:
    cpu = CPU(lines)
    cpu.run()