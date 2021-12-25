import os

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        enhancement_algorithm, image = file.read().strip().split('\n\n')
        file.close()
    image = [[x for x in row] for row in image.split('\n')]
    return enhancement_algorithm, make_bigger(image, '.')

def make_bigger(lines, end_points):
    lines = [[end_points for _ in range(len(lines[0])+2)]]+ \
            [[end_points]+row+[end_points] for row in lines] +\
            [[end_points for _ in range(len(lines[0])+2)]]
    return lines

def pixels_to_binary(pixels):
    change = {'.':'0', '#':'1'}
    binary = ''
    for p in pixels:
        binary += change[p]
    return binary

def binary_to_decimal(binary): # 1011 -> 1101 -> 2^0 + 2^1 + 2^3 = 1+2+8 = 11
    decimal = 0
    for i, b in enumerate(binary[::-1]):
        if b == '1':
            decimal += 2**i
    return decimal


class Image:
    def __init__(self, enhancement_algorithm, image):
        self.enhancement_algorithm = enhancement_algorithm
        self.image = image
        self.end_points = '.'
        self.change_emd_points = {'.':self.enhancement_algorithm[0], '#': self.enhancement_algorithm[-1]}
    
    def enhance(self):
        old_image = make_bigger(self.image, self.end_points)
        self.end_points = self.change_emd_points[self.end_points]
        for i in range(len(self.image)):
            for j in range(len(self.image[0])):
                pixels = old_image[i][j:j+3]+old_image[i+1][j:j+3]+old_image[i+2][j:j+3]
                binary = pixels_to_binary(pixels)
                index = binary_to_decimal(binary)
                self.image[i][j] = self.enhancement_algorithm[index]
        self.image = make_bigger(self.image, self.end_points)
    
    def count_lit(self):
        count = 0
        for row in self.image:
            count += row.count('#')
        return count

    def run(self, N):
        for _ in range(N):
            self.enhance()
        return self.image        


# Part 1
def part1(enhancement_algorithm, image):
    image_obj = Image(enhancement_algorithm, image)
    new_image = image_obj.run(2)
    for row in new_image:
        print(''.join(row))
    print(image_obj.count_lit())

# Part 2
def part2(enhancement_algorithm, image):
    image_obj = Image(enhancement_algorithm, image)
    new_image = image_obj.run(50)
    print(image_obj.count_lit())

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec20_test.txt'
    filename = 'dec20.txt'
    filepath = os.path.join(path, filename)
    enhancement_algorithm, image = read_file(filepath)
    #part1(enhancement_algorithm, image)
    part2(enhancement_algorithm, image)
    pass