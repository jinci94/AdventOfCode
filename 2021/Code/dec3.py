import os

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split()
        file.close()
    return lines

def binary_to_dec(n):
    dec = 0
    for i, chr in enumerate(n[::-1]):
        dec += int(chr)%2 * 2**i
    return dec

# Part 1
def part1(lines):
    gamma = ''; epsilon = ''
    for i in range(len(lines[0])):
        count = {'0':0, '1':0}
        for j in range(len(lines)):
            count[lines[j][i]] += 1
        gamma += '0' if count['0'] > count['1'] else '1'
        epsilon += '0' if count['0'] <= count['1'] else '1'
    #print(binary_to_dec(gamma) * binary_to_dec(epsilon))
    return gamma, epsilon
        
# Part 2
def part2(lines):
    lines_oxygen = lines.copy(); i = 0
    while len(lines_oxygen) > 1:
        binarytype = {'0':[], '1':[]}
        for j in range(len(lines_oxygen)):
            binarytype[lines_oxygen[j][i]].append(lines_oxygen[j])

        if len(binarytype['1']) >= len(binarytype['0']):
            lines_oxygen = binarytype['1']
        else:
            lines_oxygen = binarytype['0']
        i += 1
    print(lines_oxygen)
    
    lines_CO2 = lines.copy(); i = 0
    while len(lines_CO2) > 1:
        binarytype = {'0':[], '1':[]}
        for j in range(len(lines_CO2)):
            binarytype[lines_CO2[j][i]].append(lines_CO2[j])

        if len(binarytype['0']) <= len(binarytype['1']):
            lines_CO2 = binarytype['0']
        else:
            lines_CO2 = binarytype['1']
        i += 1
    print(lines_CO2)

    print(binary_to_dec(lines_oxygen[0]) * binary_to_dec(lines_CO2[0]))

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec3_test1.txt'
    filename = 'dec3.txt'
    filename = os.path.join(path, filename)
    lines = read_file(filename)
    part1(lines)
    part2(lines)
    pass