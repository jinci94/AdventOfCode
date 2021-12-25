import os

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

def get_value(ID, values):
    if ID == 0:
        return sum(values)
    elif ID == 1:
        count = 1
        for value in values:
            count *= value
        return count
    elif ID == 2:
        return min(values)
    elif ID == 3:
        return max(values)
    elif ID == 5:
        return 1 if values[0]>values[1] else 0
    elif ID == 6:
        return 1 if values[0]<values[1] else 0
    elif ID == 7:
        return 1 if values[0]==values[1] else 0


class Packets:
    def __init__(self, line):
        self.line = line
        self.versions = []
    
    def subpacket(self):
        version = self.line[:3]
        ID = binary_to_decimal(self.line[3:6])
        self.line = self.line[6:]
        self.versions.append(binary_to_decimal(version))
        if ID == 4:
            value = ''
            while self.line[0] != '0':
                value += self.line[1:5]
                self.line = self.line[5:]
            value += self.line[1:5]
            self.count = binary_to_decimal(value)
            self.line = self.line[5:]
            return binary_to_decimal(value)
        else:
            length_type = self.line[0]
            self.line = self.line[1:]
            if length_type == '0':
                return self.length_type_0(ID)
            elif length_type == '1':
                return self.length_type_1(ID)

    def length_type_0(self, ID):
        values = []
        length = binary_to_decimal(self.line[:15])
        new_packets = Packets(self.line[15:15+length])
        while new_packets.line != '':
            value = new_packets.run()
            values.append(value)
        self.line = self.line[15+length:]
        return get_value(ID, values)
    
    def length_type_1(self, ID):
        values = []
        N = binary_to_decimal(self.line[:11])
        self.line = self.line[11:]
        for _ in range(int(N)):
            value = self.subpacket()
            values.append(value)
        return get_value(ID, values)

    def run(self):
        return self.subpacket()
        

# Part 2
def part2(line):
    binary = hexa_to_binary(line)
    obj = Packets(binary)
    value = obj.run()
    print(value)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec16.txt'      # 144595909277
    filepath = os.path.join(path, filename)
    line = read_file(filepath)
    #line = "C200B40A82"        # 3
    #line = "04005AC33890"      # 54
    #line = "880086C3E88112"    # 7
    #line = "CE00C43D881120"    # 9
    #line = "D8005AC2A8F0"      # 1
    #line = "F600BC2D8F"        # 0
    #line = "9C005AC2F8F0"      # 0
    #line = "9C0141080250320F1802104A08"  # 1
    part2(line)
