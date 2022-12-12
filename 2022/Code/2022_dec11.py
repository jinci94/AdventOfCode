import os

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split('\n\n')
        lines = [line.split('\n') for line in lines]
        file.close()
    return lines

class MonkeyN:
    def __init__(self, items):
        self.starting_items = items
        self.operation = None
        self.number1 = None
        self.number2 = None
        self.divisible_by = None
        self.if_true = None
        self.if_false = None
        self.nr_of_inspected_items = 0
    
    def nr_of_items(self):
        return len(self.starting_items)

    def add_item_to_inspect(self, item):
        self.starting_items.append(item)
    
    def inspect(self, number1, number2):
        if self.operation == '*':
            new_number = number1 * number2
        elif self.operation == '+':
            new_number = number1 + number2
        self.nr_of_inspected_items += 1
        return new_number
    
    def relief(self, number):
        return number//3
    
    def test(self, number):
        if number%self.divisible_by == 0:
            return self.if_true
        return self.if_false

    def run_with_relief(self):
        item = self.starting_items.pop(0)
        number1 = item if self.number1 == 'old' else int(self.number1)
        number2 = item if self.number2 == 'old' else int(self.number2)
        new_number = self.inspect(number1, number2)
        new_number = self.relief(new_number)    # only for part 1
        send_to = self.test(new_number)
        return new_number, send_to
    
    def run_without_relief(self, divisible_by_all):
        item = self.starting_items.pop(0)
        number1 = item if self.number1 == 'old' else int(self.number1)
        number2 = item if self.number2 == 'old' else int(self.number2)
        new_number = self.inspect(number1, number2)
        new_number %= divisible_by_all          # only for part 2
        send_to = self.test(new_number)
        return new_number, send_to

def set_up_monkeys(lines):
    monkeys = []
    for monkey in lines:
        items = [int(x) for x in monkey[1].split(': ')[1].split(', ')]
        monkeyObj = MonkeyN(items)

        operation_parts = monkey[2].split('= ')[1].split()
        monkeyObj.operation = operation_parts[1]
        monkeyObj.number1 = operation_parts[0]
        monkeyObj.number2 = operation_parts[2]

        monkeyObj.divisible_by = int(monkey[3].split()[-1])
        monkeyObj.if_true = int(monkey[4].split()[-1])
        monkeyObj.if_false = int(monkey[5].split()[-1])

        monkeys.append(monkeyObj)
    return monkeys


# Part 1
def part1(lines):
    monkeys = set_up_monkeys(lines)
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            #print(f'Monkey {i}')
            for _ in range(monkey.nr_of_items()):
                new_number, send_to = monkey.run_with_relief()
                monkeys[send_to].add_item_to_inspect(new_number)
                #print(f'  nr {new_number} to monkey {send_to}')
    
    nr_of_inspected_items_per_monkey = []
    for monkey in monkeys:
        nr_of_inspected_items_per_monkey.append(monkey.nr_of_inspected_items)
    nr_of_inspected_items_per_monkey.sort()
    print('Part 1:', nr_of_inspected_items_per_monkey[-1]*nr_of_inspected_items_per_monkey[-2])


# Part 2
def part2(lines):
    monkeys = set_up_monkeys(lines)
    divisible_by_all = 1
    for monkey in monkeys:
        divisible_by_all *= monkey.divisible_by

    for _ in range(10000):
        for monkey in monkeys:
            for _ in range(monkey.nr_of_items()):
                new_number, send_to = monkey.run_without_relief(divisible_by_all)
                monkeys[send_to].add_item_to_inspect(new_number)
    
    nr_of_inspected_items_per_monkey = []
    for monkey in monkeys:
        nr_of_inspected_items_per_monkey.append(monkey.nr_of_inspected_items)
    print(nr_of_inspected_items_per_monkey)
    nr_of_inspected_items_per_monkey.sort()
    print('Part 2:', nr_of_inspected_items_per_monkey[-1]*nr_of_inspected_items_per_monkey[-2])

if __name__ == "__main__":
    test = True
    test = False
    if test:
        path = os.path.dirname(os.path.abspath('AoC'))
        filename = "test.txt"
    else:
        path = os.path.dirname(os.path.abspath(__file__))
        filename = "2022_dec11.txt"
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)