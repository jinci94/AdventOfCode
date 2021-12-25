import os
from time import time as t

# Both version 1 and version 2 works! The code for version 2 is a little bit shorter
# (I commented out some unnecessary code in version 2)

def read_file(filepath):
    """ Returns all the lines from a file as a list """
    with open(filepath, 'r') as file:    
        lines = file.read().strip().split('\n')
        file.close()
    reboot_process = []
    for line in lines:
        cube, coordinates = line.split()
        coordinates = [tuple([int(x) for x in coord[2:].split('..')]) for coord in coordinates.split(',')]
        reboot_process.append([cube, coordinates])
    return reboot_process

# Part 1
def part1(reboot_process):
    coordinates = set()
    for line in reboot_process:
        cube, (X,Y,Z) = line
        new_coordinates = set()
        if (-50 <= X[0] and X[1] <= 50) and (-50 <= Y[0] and Y[1] <= 50) and (-50 <= Z[0] and Z[1] <= 50):
            pass
        elif (((X[0]<=-50 and X[1]>=-50) or (X[0]<=50 and X[1]>=50)) and
              ((Y[0]<=-50 and Y[1]>=-50) or (Y[0]<=50 and Y[1]>=50)) and
              ((Z[0]<=-50 and Z[1]>=-50) or (Z[0]<=50 and Z[1]>=50))):
            X = (max(X[0],-50), min(X[1],50))
            Y = (max(Y[0],-50), min(Y[1],50))
            Z = (max(Z[0],-50), min(Z[1],50))
            print(X, Y, Z)
            # Just checking if any of the "far away cubes" intersect with
            # the [-50,50]x[-50,50]x[-50,50]-cube, but it didn't.
        else:
            X = (1,0); Y = (1,0); Z = (1,0)
        for x in range(X[0], X[1]+1):
            for y in range(Y[0], Y[1]+1):
                for z in range(Z[0], Z[1]+1):
                    new_coordinates.add((x,y,z))
        if cube == 'on':
            coordinates = coordinates.union(new_coordinates)
        elif cube == 'off':
            coordinates = coordinates - new_coordinates
    count = 0
    for x, y, z in list(coordinates):
        if -50<=x<=50:
            if -50<=y<=50:
                if -50<=z<=50:
                    count += 1
    print(count)


# Part 2
def part2(reboot_process):
    count = 0
    cubes = []
    for line in reboot_process:
        light, (X,Y,Z) = line

        # Can use these two lines to get the result for part 1: (faster)
        #if X[0]>50 or X[1]<-50 or Y[0]>50 or Y[1]<-50 or Z[0]>50 or Z[1]<-50:
        #    break

        new_cubes = []; indices = []
        for i,(x,y,z) in enumerate(cubes):
            if ((x[1]>=X[0] and x[0]<=X[1]) and
                (y[1]>=Y[0] and y[0]<=Y[1]) and
                (z[1]>=Z[0] and z[0]<=Z[1])):
                indices.append(i)

                # Check for X:
                """
                if any([any([x[i]==X[j] for i in [0,1]]) for j in [0,1]]):
                    if X[0]<=x[0] and x[1]<=X[1]:
                        x_next = (x[0], x[1])
                    elif X[0]==x[0]:    # then x[1]>X[1] because of above
                        x_new = (X[1]+1,x[1])
                        x_next = (x[0],X[1])
                        new_cubes.append((x_new, y, z))
                    elif X[1]==x[1]:
                        x_new = (x[0],X[0]-1)
                        x_next = (X[0],x[1])
                        new_cubes.append((x_new, y, z))
                    elif X[0]==x[1]:
                        x_new = (x[0],X[0]-1)
                        x_next = (x[1],x[1])
                        new_cubes.append((x_new, y, z))
                    elif X[1]==x[0]:
                        x_new = (X[1]+1,x[1])
                        x_next = (x[0],x[0])
                        new_cubes.append((x_new, y, z))
                """
                if x[0]<=X[0] and X[1]<=x[1]:
                    x_new1 = (x[0], X[0]-1)
                    x_new2 = (X[1]+1, x[1])
                    x_next = (X[0], X[1])
                    new_cubes.append((x_new1, y, z))
                    new_cubes.append((x_new2, y, z))
                elif x[0]<=X[0]<=x[1]:
                    x_new = (x[0], X[0]-1)
                    x_next = (X[0], x[1])
                    new_cubes.append((x_new, y, z))
                elif x[0]<=X[1]<=x[1]:
                    x_new = (X[1]+1, x[1])
                    x_next = (x[0], X[1])
                    new_cubes.append((x_new, y, z))
                else:
                    x_next = (x[0], x[1])

                # Check for Y:
                """
                if any([any([y[i]==Y[j] for i in [0,1]]) for j in [0,1]]):
                    if Y[0]<=y[0] and y[1]<=Y[1]:
                        y_next = (y[0], y[1])
                    elif Y[0]==y[0]:    # then x[1]>X[1] because of above
                        y_new = (Y[1]+1,y[1])
                        y_next = (y[0],Y[1])
                        new_cubes.append((x_next, y_new, z))
                    elif Y[1]==y[1]:
                        y_new = (y[0],Y[0]-1)
                        y_next = (Y[0],y[1])
                        new_cubes.append((x_next, y_new, z))
                    elif Y[0]==y[1]:
                        y_new = (y[0],Y[0]-1)
                        y_next = (y[1],y[1])
                        new_cubes.append((x_next, y_new, z))
                    elif Y[1]==y[0]:
                        y_new = (Y[1]+1,y[1])
                        y_next = (y[0],y[0])
                        new_cubes.append((x_next, y_new, z))
                """
                if y[0]<=Y[0] and Y[1]<=y[1]:
                    y_new1 = (y[0], Y[0]-1)
                    y_new2 = (Y[1]+1, y[1])
                    y_next = (Y[0], Y[1])
                    new_cubes.append((x_next, y_new1, z))
                    new_cubes.append((x_next, y_new2, z))
                elif y[0]<=Y[0]<=y[1]:
                    y_new = (y[0], Y[0]-1)
                    y_next = (Y[0], y[1])
                    new_cubes.append((x_next, y_new, z))
                elif y[0]<=Y[1]<=y[1]:
                    y_new = (Y[1]+1, y[1])
                    y_next = (y[0], Y[1])
                    new_cubes.append((x_next, y_new, z))
                else:
                    y_next = (y[0], y[1])

                # Check for Z:
                """
                if any([any([z[i]==Z[j] for i in [0,1]]) for j in [0,1]]):
                    if Z[0]<=z[0] and z[1]<=Z[1]:
                        z_next = (z[0], z[1])
                    elif Z[0]==z[0]:    # then x[1]>X[1] because of above
                        z_new = (Z[1]+1,z[1])
                        new_cubes.append((x_next, y_next, z_new))
                    elif Z[1]==z[1]:
                        z_new = (z[0],Z[0]-1)
                        new_cubes.append((x_next, y_next, z_new))
                    elif Z[0]==z[1]:
                        z_new = (z[0],Z[0]-1)
                        new_cubes.append((x_next, y_next, z_new))
                    elif Z[1]==z[0]:
                        z_new = (Z[1]+1,z[1])
                        new_cubes.append((x_next, y_next, z_new))
                """
                if z[0]<=Z[0] and Z[1]<=z[1]:
                    z_new1 = (z[0], Z[0]-1)
                    z_new2 = (Z[1]+1, z[1])
                    new_cubes.append((x_next, y_next, z_new1))
                    new_cubes.append((x_next, y_next, z_new2))
                elif z[0]<=Z[0]<=z[1]:
                    z_new = (z[0], Z[0]-1)
                    new_cubes.append((x_next, y_next, z_new))
                elif z[0]<=Z[1]<=z[1]:
                    z_new = (Z[1]+1, z[1])
                    new_cubes.append((x_next, y_next, z_new))

        # remove the cubes that intersect with the new one, and add the pieces:
        for i, index in enumerate(indices):
            cubes.pop(index-i)
        cubes += new_cubes
        
        # if light is on, add the new cube
        if light == 'on':
            cubes.append((X,Y,Z))

    for x,y,z in cubes:
        #assert (x[1]-x[0]+1)*(y[1]-y[0]+1)*(z[1]-z[0]+1) > 0, f'{x},{y},{z}'
        count += (x[1]-x[0]+1)*(y[1]-y[0]+1)*(z[1]-z[0]+1)
    print(count)


if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = 'dec22_test1.txt' # part1: 590784
    filename = 'dec22_test2.txt' # part1: 474140, part2: 2758514936282235
    filename = 'dec22.txt'       # part1: 615869, part2: 1323862415207825
    filepath = os.path.join(path, filename)
    reboot_process = read_file(filepath)
    #part1(reboot_process)
    t1 = t()
    part2(reboot_process)
    t2 = t()
    print(t2-t1)