import os

"""
problem jag stötte på:
- missförstod reglerna i del 2. Jag trodde det var liknande regler som del 1,
  dvs att man inte kunde se träd som var kortare än de föregående träden, men
  man kunde tydligen se alla träd, så länge de var kortare än trädet man stod på.
  Jag testade därför 3 olika lösningar (typ 1, 2 och 3) för att se skillnaden.

Typ 1: (Det dom menade)
Du kan se alla träd, så länge de är kortare än trädet du står på.

Typ 2: (Min tolkning)
Liknande del 1 kan man här bara se trädet ifall alla träd som ligger
mellan dig och det trädet du kollar på är kortare eller lika långa som 
det trädet du kollar på. 

Typ 3: (Verkligt - mellan 1 och 2)
Du kan bara se ett träd ifall de träden som står mellan dig och trädet
inte skymmer trädet du försöker se. Om du tex drar ett snöre mellan
toppen av trädet du står på och toppen av trädet du kollar på, så att
snöret är helt rakt, kommer du inte kunna se trädet ifall snöret måste
passera genom andra träd påväg till trädet du ser på. Men om snöret kan
sträckas ut mellan de två trädtopparna utan att vidröra de andra träden
så kommer du kunna se det. Här använder jag formeln för lutningen av
en linjär ekvation, dvs k = dy/dx som vi räknar ut genom:
k = abs(längden på träd 1 - längden på träd 2)/(avståndet mellan de två träden)
För varje träd bortanför de andra träden måste k antingen vara samma
eller bli mindre för att vi ska kunna se trädet.

Gäller alla typer:
Om ett träd är lika långt som trädet du står på kan du se det trädet,
men inga träd bortanför.
"""

def read_file(filename):
    """ Returns all the lines from a file as a list """
    with open(filename, 'r') as file:    
        lines = file.read().strip().split()
        lines = [[int(x) for x in line] for line in lines]
        file.close()
    return lines

# Part 1
def part1(trees):
    visible_trees = [['.' for _ in line] for line in lines]
    # the border:
    for i in range(len(visible_trees)):
        for j in range(len(visible_trees[i])):
            if i == 0 or j == 0 or i == len(visible_trees)-1 or j == len(visible_trees[i])-1:
                visible_trees[i][j] = '#'
    # the inner trees:
    # left to right:
    for i, row in enumerate(trees[1:-1], start=1):
        for j, tree in enumerate(row[1:-1], start=1):
            highest_tree = 0
            for k in range(0,j):
                highest_tree = max(row[k],highest_tree)
            if tree > highest_tree:
                visible_trees[i][j] = '#'
    # right to left:
    for i, row in enumerate(trees[1:-1], start=1):
        for j, tree in enumerate(row[1:-1], start=1):
            highest_tree = 0
            for k in range(j+1, len(row)):
                highest_tree = max(row[k],highest_tree)
            if tree > highest_tree:
                visible_trees[i][j] = '#'
    # top to bottom:
    for i, row in enumerate(trees[1:-1], start=1):
        for j, tree in enumerate(row[1:-1], start=1):
            highest_tree = 0
            for k in range(0, i):
                highest_tree = max(trees[k][j],highest_tree)
            if tree > highest_tree:
                visible_trees[i][j] = '#'
    # bottom to top:
    for i, row in enumerate(trees[1:-1], start=1):
        for j, tree in enumerate(row[1:-1], start=1):
            highest_tree = 0
            for k in range(i+1, len(trees)):
                highest_tree = max(trees[k][j],highest_tree)
            if tree > highest_tree:
                visible_trees[i][j] = '#'
    # count:
    count = 0
    for trees in visible_trees:
        for tree in trees:
            if tree == '#':
                count += 1
    print(count)


# Part 2
def part2(trees):
    highest_score1 = 0
    highest_score2 = 0
    highest_score3 = 0
    for i in range(1,len(trees)-1):
        for j in range(1,len(trees[i])-1):
            count_type1 = [0,0,0,0] # ser alla träd lägre än X
            count_type2 = [0,0,0,0] # ser alla träd högre än de tidigare men kortare än X
            count_type3 = [0,0,0,0] # ser träden linjärt (som verkligheten)
            # to left:
            highest = 0; gradient = 10
            for k in range(j,0,-1):
                if trees[i][k-1] >= trees[i][j]:
                    count_type1[0] += 1
                    count_type2[0] += 1
                    count_type3[0] += 1
                    break
                if trees[i][k-1] >= highest:
                    highest = trees[i][k-1]
                    count_type2[0] += 1
                if abs(trees[i][j] - trees[i][k-1])/abs(j - (k-1)) <= gradient:
                    gradient = abs(trees[i][j] - trees[i][k-1])/abs(j - (k-1))
                    count_type3[0] += 1
                count_type1[0] += 1
            # to right:
            highest = 0; gradient = 10
            for k in range(j+1,len(trees[i])):
                if trees[i][k] >= trees[i][j]:
                    count_type1[1] += 1
                    count_type2[1] += 1
                    count_type3[1] += 1
                    break
                if trees[i][k] >= highest:
                    highest = trees[i][k]
                    count_type2[1] += 1
                if abs(trees[i][j] - trees[i][k])/abs(j - k) <= gradient:
                    gradient = abs(trees[i][j] - trees[i][k])/abs(j - k)
                    count_type3[1] += 1
                count_type1[1] += 1
            # to top:
            highest = 0; gradient = 10
            for k in range(i,0,-1):
                if trees[k-1][j] >= trees[i][j]:
                    count_type1[2] += 1
                    count_type2[2] += 1
                    count_type3[2] += 1
                    break
                if trees[k-1][j] >= highest:
                    highest = trees[k-1][j]
                    count_type2[2] += 1
                if abs(trees[i][j] - trees[k-1][j])/abs(i - (k-1)) <= gradient:
                    gradient = abs(trees[i][j] - trees[k-1][j])/abs(i - (k-1))
                    count_type3[2] += 1
                count_type1[2] += 1
            # to bottom:
            highest = 0; gradient = 10
            for k in range(i+1,len(trees)):
                if trees[k][j] >= trees[i][j]:
                    count_type1[3] += 1
                    count_type2[3] += 1
                    count_type3[3] += 1
                    break
                if trees[k][j] >= highest:
                    highest = trees[k][j]
                    count_type2[3] += 1
                if abs(trees[i][j] - trees[k][j])/abs(i - k) <= gradient:
                    gradient = abs(trees[i][j] - trees[k][j])/abs(i - k)
                    count_type3[3] += 1
                count_type1[3] += 1

            # count:
            scenic_score1 = 1; scenic_score2 = 1; scenic_score3 = 1
            for nr1, nr2, nr3 in zip(count_type1, count_type2, count_type3):
                scenic_score1 *= nr1
                scenic_score2 *= nr2
                scenic_score3 *= nr3
            highest_score1 = max(highest_score1, scenic_score1)
            highest_score2 = max(highest_score2, scenic_score2)
            highest_score3 = max(highest_score3, scenic_score3)
    print(highest_score1, highest_score2, highest_score3)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = "test.txt"
    filename = "2022_dec8_eget_test.txt"
    #filename = "2022_dec8.txt"
    filepath = os.path.join(path, filename)
    lines = read_file(filepath)
    part1(lines)
    part2(lines)