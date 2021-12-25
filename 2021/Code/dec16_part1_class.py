import os

# December 16. Part 1: Solved by using a recursive class

"""
I solved part 1 in two ways (loop & class) because I
thought the code did't work and I couldn't figure out why.

I first wrote the code for "class", and then I wrote
the code for "loop", but I got the same results in both.
Then I realized that I had just looked for the "test-answer"
in the description in the wrong line...

So for part 2 I just used the "best suited one" from part 1.
"""

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        line = file.read().strip()
        file.close()
    return line

# created in another file:
hexabinary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
binaryhexa = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

def binary_to_decimal(binary):
    decimal = 0
    for i, b in enumerate(binary[::-1]):
        if int(b)%2 == 1:
            decimal += 2**i
    return decimal

def hexa_to_binary(hexa):
    binary = ''
    for h in hexa:
        binary += hexabinary[h]
    return binary

# Part 1
class Packets:
    def __init__(self, line):
        self.line = line
        self.versions = []
    
    def subpacket(self):
        version = self.line[:3]
        ID = self.line[3:6]
        self.line = self.line[6:]
        self.versions.append(binary_to_decimal(version))
        if binary_to_decimal(ID) == 4:
            while self.line[0] != '0':
                self.line = self.line[5:]
            self.line = self.line[5:]
        else:
            length_type = self.line[0]
            self.line = self.line[1:]
            if length_type == '0':
                self.length_type_0()
            elif length_type == '1':
                self.length_type_1()

    def length_type_0(self):
        length = binary_to_decimal(self.line[:15])
        new_packets = Packets(self.line[15:15+length])
        while new_packets.line != '':
            versions = new_packets.run()
        self.versions += versions
        self.line = self.line[15+length:]
    
    def length_type_1(self):
        N = binary_to_decimal(self.line[:11])
        self.line = self.line[11:]
        for _ in range(int(N)):
            self.subpacket()

    def run(self):
        self.subpacket()
        return self.versions
        

def part1(line):
    binary = hexa_to_binary(line)
    obj = Packets(binary)
    versions = obj.run()
    print(versions)
    print(sum(versions))


if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec16.txt'                      # 993
    filepath = os.path.join(path, filename)
    line = read_file(filepath)
    #line = "8A004A801A8002F478"                # 16
    #line = "620080001611562C8802118E34"        # 12
    #line = "C0015000016115A2E0802F182340"      # 23
    #line = "A0016C880162017C3686B18A3D4780"    # 31
    part1(line)
