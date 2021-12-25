import os

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    lines = [line.split(' | ') for line in lines]
    return lines

# Part 1
def part1(lines):
    count = 0
    for signal_pattern ,output in lines:
        output = output.split()
        for o in output:
            if len(o) in [2,3,4,7]:
                count += 1
    print(count)


# Part 2
class Numbers:
    def __init__(self, signal_pattern):
        self.signal_pattern = signal_pattern
        self.digits = {nr: None for nr in range(10)}
        self.ccc = None
        self.eee = None
        """
        example positions:
         aaaa    
        b    c
        b    c
         dddd 
        e    f
        e    f
         gggg 
        """
    
    def find_1(self):
        for nr in self.signal_pattern:
            if len(nr) == 2:
                self.digits[1] = nr
                self.signal_pattern.remove(nr)
    def find_7(self):
        for nr in self.signal_pattern:
            if len(nr) == 3:
                self.digits[7] = nr
                self.signal_pattern.remove(nr)
    def find_4(self):
        for nr in self.signal_pattern:
            if len(nr) == 4:
                self.digits[4] = nr
                self.signal_pattern.remove(nr)
    def find_8(self):
        for nr in self.signal_pattern:
            if len(nr) == 7:
                self.digits[8] = nr
                self.signal_pattern.remove(nr)
    def find_6(self):
        for nr in self.signal_pattern:
            if len(nr) == 6 and not all([(x in nr) for x in self.digits[1]]):
                self.digits[6] = nr
                self.ccc = self.digits[1][0] if self.digits[1][0] not in nr else self.digits[1][1]
                self.signal_pattern.remove(nr)
    def find_5(self):
        for nr in self.signal_pattern:
            if len(nr) == 5 and self.ccc not in nr:
                self.digits[5] = nr
                all_5 = [x for x in nr]
                self.eee = list(set([x for x in 'abcdefg']) - set(all_5) - set([self.ccc]))[0]
                self.signal_pattern.remove(nr)
    def find_9(self):
        for nr in self.signal_pattern:
            if len(nr) == 6 and self.eee not in nr:
                self.digits[9] = nr
                self.signal_pattern.remove(nr)
    def find_0(self):
        for nr in self.signal_pattern:
            if len(nr) == 6:
                self.digits[0] = nr
                self.signal_pattern.remove(nr)
    def find_2(self):
        for nr in self.signal_pattern:
            if self.eee in nr:
                self.digits[2] = nr
                self.signal_pattern.remove(nr)
    def find_3(self):
        self.digits[3] = self.signal_pattern[0]
        self.signal_pattern.pop()

    def find_all(self):
        self.find_1()
        self.find_7()
        self.find_4()
        self.find_8()
        self.find_6()
        self.find_5()
        self.find_9()
        self.find_0()
        self.find_2()
        self.find_3()

    def get_numbers(self):
        self.find_all()
        return {''.join(sorted([x for x in item])):key for key, item in self.digits.items()}


def part2(lines):
    count = 0
    for signal_pattern ,output in lines:
        signal_pattern = signal_pattern.split()
        output = output.split()
        
        numbers = Numbers(signal_pattern)
        digits = numbers.get_numbers()
        number = ''
        for digit in output:
            number += str(digits[''.join(sorted([x for x in digit]))])
        count += int(number)
    print(count)



if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec8_test.txt'
    filename = 'dec8.txt'
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    #part1(lines)
    part2(lines)
