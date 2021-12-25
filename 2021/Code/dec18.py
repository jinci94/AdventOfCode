import os

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    return lines

def explode(line):
    order = 0
    for i, ch in enumerate(line):
        if ch == '[':
            order += 1
        elif ch == ']':
            order -= 1
        elif ch == ',':
            continue
        elif order > 4:
            before = line[:i-1] # don't include [
            end = line.find(']', i)
            nr1, nr2 = line[i:end].split(',')
            after = line[end+1:] # don't include ]

            if before.count('[')+before.count(',')+before.count(']') != len(before):
                j = len(before)-1
                while before[j] in '[,]':
                    j -= 1
                if before[j-1] in '[,]':
                    before = before[:j] + str(int(before[j])+int(nr1)) + before[j+1:]
                else:
                    before = before[:j-1] + str(int(before[j-1:j+1])+int(nr1)) + before[j+1:]

            if after.count('[')+after.count(',')+after.count(']') != len(after):
                j = 0
                while after[j] in '[,]':
                    j += 1
                if after[j+1] in '[,]':
                    after = after[:j] + str(int(after[j])+int(nr2)) + after[j+1:]
                else:
                    after = after[:j] + str(int(after[j:j+2])+int(nr2)) + after[j+2:]

            new_line = before + '0' + after
            return reduce(new_line)
    return line

def split(line):
    order = 0
    for i, ch in enumerate(line):
        if ch == '[':
            order += 1
        elif ch == ']':
            order -= 1
        elif ch == ',':
            continue
        elif line[i+1] in '0123456789':
            new_line = line[:i]
            nr = int(line[i:i+2])
            new_line += '[' + str(nr//2) + ',' + str((nr+1)//2) + ']'
            new_line += line[i+2:]
            return reduce(new_line)
    return line

def reduce(line):
    line = explode(line)
    line = split(line)
    return line

# Explode:
assert reduce('[[[[[9,8],1],2],3],4]') == '[[[[0,9],2],3],4]'
assert reduce('[7,[6,[5,[4,[3,2]]]]]') == '[7,[6,[5,[7,0]]]]'
assert reduce('[[6,[5,[4,[3,2]]]],1]') == '[[6,[5,[7,0]]],3]'
assert reduce('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]') == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'

# Split:
assert reduce('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]') == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'

def magnitude(line, order):
    if order == 0:
        return line
    this_order = 0
    for i, ch in enumerate(line):
        if ch == '[':
            this_order += 1
        elif ch == ']':
            this_order -= 1
        elif ch == ',':
            continue
        elif this_order == order:
            before = line[:i-1] # don't include [
            end = line.find(']', i)
            nr1, nr2 = line[i:end].split(',')
            after = line[end+1:] # don't include ]
            new_line = before + str(3*int(nr1)+2*int(nr2)) + after
            return magnitude(new_line, order)
    return magnitude(line, order-1)

assert magnitude('[[1,2],[[3,4],5]]', 4) == '143'
assert magnitude('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', 4) == '1384'
assert magnitude('[[[[1,1],[2,2]],[3,3]],[4,4]]', 4) == '445'
assert magnitude('[[[[3,0],[5,3]],[4,4]],[5,5]]', 4) == '791'
assert magnitude('[[[[5,0],[7,4]],[5,5]],[6,6]]', 4) == '1137'
assert magnitude('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]', 4) == '3488'

# Part 1
def part1(lines):
    first_part = reduce(lines[0])
    for second_part in lines[1:]:
        #print(first_part)
        first_part = reduce('['+first_part+','+second_part+']')
    mag = magnitude(first_part, 4)
    print(mag)
        


# Part 2
def part2(lines):
    max_magnitude = 0
    for first_part in lines:
        for second_part in lines:
            if first_part != second_part:
                added = reduce('['+first_part+','+second_part+']')
                mag = magnitude(added, 4)
                max_magnitude = max(max_magnitude, int(mag))
    print(max_magnitude)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec18_test1.txt'
    filename = 'dec18_test2.txt'
    filename = 'dec18_test3.txt'
    filename = 'dec18_test4.txt'
    filename = 'dec18_test5.txt'
    filename = 'dec18.txt'
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)
    pass