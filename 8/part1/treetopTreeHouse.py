#!/usr/bin/env python3

def checkHorizontally(treeCoor, grid):
    treeCheckedSize = grid[treeCoor[0]][treeCoor[1]]
    sidesVisibility = [True, True]
    for treeY in range(len(grid[treeCoor[0]])):
        if treeY != treeCoor[1] and treeCheckedSize <= grid[treeCoor[0]][treeY]:
            if treeY < treeCoor[1]:
                sidesVisibility[0] = False
            else:
                sidesVisibility[1] = False
            if sidesVisibility == [False, False]:
                return False
    return True

def checkVertically(treeCoor, grid):
    treeCheckedSize = grid[treeCoor[0]][treeCoor[1]]
    sidesVisibility = [True, True]
    for treeX in range(len(grid)):
        if treeX != treeCoor[0] and treeCheckedSize <= grid[treeX][treeCoor[1]]:
            if treeX < treeCoor[0]:
                sidesVisibility[0] = False
            else:
                sidesVisibility[1] = False
            if sidesVisibility == [False, False]:
                return False
    return True

grid = []
visibleTrees = 0

with open("../input.txt") as inputFile:
    for line in inputFile:
        grid.append([int(tree) for tree in line.strip()])

lineMinMax = [0, len(grid)-1]
colMinMax = [0, len(grid[0])-1]

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if x in lineMinMax or y in colMinMax:
            visibleTrees += 1
        elif checkHorizontally([x,y], grid) or checkVertically([x,y], grid):
            visibleTrees += 1


print(visibleTrees)
