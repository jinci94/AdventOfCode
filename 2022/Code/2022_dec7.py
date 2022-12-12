from functools import reduce
import collections.abc
import os

"""
problem jag stötte på:
- mapparna kan ha samma namn
"""

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        line = file.read().strip().split('\n')
        file.close()
    return line

class FileSystem:
    def __init__(self, lines):
        self.lines = lines
        self.file_system = {}
        self.current_path = []
        self.dir_memory = {}  # path: memory
        self.nr = 0
    
    def update_file_system(self, this_dic, this_dir, new_val):
        if len(this_dir) == 1:
            this_dic[this_dir[0]] = new_val
        else:
            this_dic[this_dir[0]] = self.update_file_system(this_dic[this_dir[0]], this_dir[1:], new_val)
        return this_dic

    def executed_commands(self, line, lines):
        command = line.split()
        if command[1] == 'cd':
            if command[2] == '..':
                self.current_path.pop()
            elif command[1] == '/':
                self.current_path = ['/']
            else:
                self.current_path.append(command[2])
                self.dir_memory[' -> '.join(self.current_path.copy())] = 0
        elif command[1] == 'ls':
            files = dict()
            for file in lines[1:]:
                if file[0] == '$':
                    break
                file = file.split()
                if file[0] == 'dir':
                    files[file[1]] = dict()
                else:
                    files[f'file_{self.nr}'] = (file[1], int(file[0]))
                    self.nr += 1
            self.file_system = self.update_file_system(self.file_system, self.current_path, files)

    def get_memory(self, this_dic, this_dir):
        if len(this_dir) == 1:
            memory = 0
            for key, value in this_dic[this_dir[0]].items():
                if 'file' in key:
                    memory += value[1]
        else:
            memory = self.get_memory(this_dic[this_dir[0]], this_dir[1:])
        return memory

    def count_memory(self):
        for key in self.dir_memory:
            this_memory = self.get_memory(self.file_system, key.split(' -> '))
            self.dir_memory[key] = this_memory
        
        for key in self.dir_memory:
            for other_key in self.dir_memory:
                if (other_key != key and other_key.startswith(key)):
                    self.dir_memory[key] += self.dir_memory[other_key]
        return self.dir_memory
    
    def print_system(self, this_dict, tab=''):
        for key, value in this_dict.items():
            if 'file' in key:
                print(tab, value)
            else:
                print(tab, 'dict', key)
                this_tab = tab + '  '
                self.print_system(this_dict[key], tab=this_tab)

    def run1(self):
        for i, line in enumerate(self.lines):
            if line[0] == '$':
                self.executed_commands(line, self.lines[i:])
        memory = self.count_memory()
        count = 0
        for _, value in memory.items():
            if value <= 100000:
                count += value
        print(count)
        #self.print_system(self.file_system)

    def run2(self):
        for i, line in enumerate(self.lines):
            if line[0] == '$':
                self.executed_commands(line, self.lines[i:])
        memory = self.count_memory()

        disk_space = 70000000
        update = 30000000
        used = memory['/']
        free_space = disk_space - used
        need_to_delete = update - free_space

        can_delete = []
        for _, value in memory.items():
            if value >= need_to_delete:
                can_delete.append(value)
        print(min(can_delete))


# Part 1
def part1(lines):
    fileSystemObj = FileSystem(lines)
    fileSystemObj.run1()

# Part 2
def part2(lines):
    fileSystemObj = FileSystem(lines)
    fileSystemObj.run2()

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = "test.txt"                   # 95437   , 24933642
    filename = "2022_dec7_eget_test.txt"    # 120.000 , -
    filename = "2022_dec7.txt"              # 2031851 , 2568781
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)