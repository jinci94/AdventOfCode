import os

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        days = list(map(int,file.read().strip().split(',')))
        file.close()
    return days

# Part 1
def part1(days):
    for _ in range(80):
        temp_day = days.copy()
        for i,day in enumerate(days):
            if day == 0:
                temp_day[i] = 6
                temp_day.append(8)
            else:
                temp_day[i] -= 1
        days = temp_day
    print(len(days))

# Part 2
def part2(days):
    check_time = 256

    fishes = {day:0 for day in range(7)}
    for day in days:
        fishes[day] += 1
    
    for i in range(check_time):
        temp_fishes = {day:0 for day in range(9)}
        for day, nr in fishes.items():
            if day == 0:
                temp_fishes[6] += nr
                temp_fishes[8] += nr
            else:
                temp_fishes[day-1] += nr
        fishes = temp_fishes
    number_of_fishes = sum([nr for fish, nr in fishes.items()])
    print(number_of_fishes)


if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec6_test.txt'
    filename = 'dec6.txt'
    filepath = os.path.join(path, filename)
    days = read_file(filepath)
    #part1(days)
    part2(days)
