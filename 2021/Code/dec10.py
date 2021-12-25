import os

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    return lines

# Part 1
def corrupted(line):
    operator = {'(':')', '[':']', '{':'}', '<':'>'}
    point = {')':3, ']':57, '}':1197, '>':25137}
    temp_next = [line[0]]
    for i in range(1,len(line)):
        if temp_next and line[i] == operator[temp_next[-1]]:
            temp_next.pop(-1)
        elif line[i] in operator:
            temp_next.append(line[i])
        else:
            return point[line[i]]
    return 0

def part1(lines):
    count = 0
    for line in lines:
        count += corrupted(line)
    print(count)

# Part 2
def incomplete(line):
    operator = {'(':')', '[':']', '{':'}', '<':'>'}
    temp_next = [line[0]]
    for i in range(1,len(line)):
        if temp_next and line[i] == operator[temp_next[-1]]:
            temp_next.pop(-1)
        elif line[i] in operator:
            temp_next.append(line[i])
        else:
            return []
    incomplete_op = [operator[ch] for ch in temp_next[::-1]]
    return incomplete_op

def part2(lines):
    point = {')':1, ']':2, '}':3, '>':4}
    total_score = []
    for line in lines:
        count = 0
        for ch in incomplete(line):
            count *= 5
            count += point[ch]
        if count != 0:
            total_score.append(count)
    print(sorted(total_score)[len(total_score)//2])

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec10_test.txt'
    filename = 'dec10.txt'
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)
    pass