#!/usr/bin/env python3

def checkHorizontally(treeCoor, grid):
    treeCheckedSize = grid[treeCoor[0]][treeCoor[1]]
    sidesVisibility = [0, 0]
    # left
    for treeY in range(treeCoor[1]-1, -1, -1):
        sidesVisibility[0] += 1
        if treeCheckedSize <= grid[treeCoor[0]][treeY]:
            break
    # right
    for treeY in range(treeCoor[1]+1, len(grid[treeCoor[0]])):
        sidesVisibility[1] += 1
        if treeCheckedSize <= grid[treeCoor[0]][treeY]:
            break
    return sidesVisibility[0] * sidesVisibility[1]

def checkVertically(treeCoor, grid):
    treeCheckedSize = grid[treeCoor[0]][treeCoor[1]]
    sidesVisibility = [0, 0]
    # top
    for treeX in range(treeCoor[0]-1, -1, -1):
        sidesVisibility[0] += 1
        if treeCheckedSize <= grid[treeX][treeCoor[1]]:
            break
    # bottom
    for treeX in range(treeCoor[0]+1, len(grid)):
        sidesVisibility[1] += 1
        if treeCheckedSize <= grid[treeX][treeCoor[1]]:
            break
    return sidesVisibility[0] * sidesVisibility[1]


grid = []
visibleTrees = 0
highestScenicScore = 0

with open("../input.txt") as inputFile:
    for line in inputFile:
        grid.append([int(tree) for tree in line.strip()])

lineMinMax = [0, len(grid)-1]
colMinMax = [0, len(grid[0])-1]

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if x not in lineMinMax and y not in colMinMax:
            scenicScore = checkHorizontally([x,y], grid) * checkVertically([x,y], grid)
            highestScenicScore = scenicScore if scenicScore > highestScenicScore else highestScenicScore

print(highestScenicScore)
