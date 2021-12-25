import os
from collections import Counter

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n\n')
        file.close()
    template, rules = lines
    template = [x for x in template]
    rules = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in rules.split('\n')}
    return template, rules

# Part 1
def count(template):
    all = list(set(template))
    max_letter = None; min_letter = None
    maximum = 0; minimum = 1e6
    for a in all:
        count = template.count(a)
        if count < minimum:
            minimum = count
            min_letter = a
        if count > maximum:
            maximum = count
            max_letter = a
    print(maximum - minimum)

def part1(filepath):
    template, rules = read_file(filepath)
    for _ in range(10):
        for i in range(0, len(template)*2-2, 2):
            template.insert(i+1, rules[''.join(template[i:i+2])])
    count(template)

# Part 2
def part2(filepath):
    template, rules = read_file(filepath)
    polymer = {}
    for i in range(len(template)-1):
        key = template[i]+template[i+1]
        if key not in polymer:
            polymer[key] = 0
        polymer[key] += 1

    for _ in range(40):
        temp_polymer = {}
        for key in polymer:
            # for polymer=...ac..., key=ac and rule[ac]=b => polymer=...abc...
            a = key[0]; c = key[1]
            b = rules[key]
            ab = a + b
            bc = b + c
            if ab not in temp_polymer:
                temp_polymer[ab] = 0
            if bc not in temp_polymer:
                temp_polymer[bc] = 0
            temp_polymer[ab] += polymer[key]
            temp_polymer[bc] += polymer[key]
        polymer = temp_polymer

    letters = list(set([key[0] for key in polymer]))
    count_letters = {letter:0 for letter in letters}
    for key in polymer:
        count_letters[key[0]] += polymer[key]
    count_letters[template[-1]] += 1

    max_letter = None; min_letter = None
    maximum = 0; minimum = 1e100
    for letter, count in count_letters.items():
        if count > maximum:
            maximum = count
            max_letter = letter
        if count < minimum:
            minimum = count
            min_letter = letter
    print(maximum - minimum)
        

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec14_test.txt'
    filename = 'dec14.txt'
    filepath = os.path.join(path, filename)
    part1(filepath)
    part2(filepath)
