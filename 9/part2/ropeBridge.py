#!/usr/bin/env python3
import math

NB_KNOTS = 10
knotsCoord = {}
lastKnotPos = []
lastVector = []

def getDistance(head, tail):
    return max(int(abs(head[0]-tail[0])), int(abs(head[1]-tail[1])))

def parseCoord(coor):
    return f"{coor[0]},{coor[1]}"

def moveCoor(coor, side):
    if side == "L":
        coor[0] -= 1
    elif side == "R":
        coor[0] += 1
    elif side == "U":
        coor[1] += 1
    elif side == "D":
        coor[1] -= 1
    return coor

def getTailCoord(head, tail):
    moveNeeded = [math.copysign(1, head[0]-tail[0]), math.copysign(1, head[1]-tail[1])]
    return [int(tail[0]+moveNeeded[0]), int(tail[1]+moveNeeded[1])]

# don't work for real input, make the range bigger
def genTable(allPos):
    for lineNb in range(15,-6,-1):
        line = ''
        for colNb in range(-11,15):
            colChecked = False
            for knotNb, knotCoord in allPos.items():
                if knotCoord[0] == colNb and knotCoord[1] == lineNb and not colChecked:
                    line += str(knotNb)
                    colChecked = True
            if not colChecked:
                line += '.'
            if colNb == 0 and lineNb == 0:
                line = line[:-1]
                line += 'S'
        print(line)
    print()


with open("../input.txt") as inputFile:
    # Init knots
    for i in range(NB_KNOTS):
        knotsCoord[i] = [0, 0]
    # Solve
    for move in inputFile:
        print(f'-- {move} headpos - {knotsCoord[1]} --')
        move = move.strip().split()
        for i in range(int(move[1])):
            knotsCoord[0] = moveCoor(knotsCoord[0], move[0]) # Move head
            print(f'---------- {i+1} ------------')
            for knotIndex in range(1, len(knotsCoord)):
                headIndex = knotIndex-1
                if getDistance(knotsCoord[headIndex], knotsCoord[knotIndex]) > 1: # Check if head in perimeter, if so move
                    if knotsCoord[headIndex][0] == knotsCoord[knotIndex][0]: # same line
                        if knotsCoord[headIndex][1] > knotsCoord[knotIndex][1]:
                            knotsCoord[knotIndex] = moveCoor(knotsCoord[knotIndex], 'U') # Follow head's move
                        else:
                            knotsCoord[knotIndex] = moveCoor(knotsCoord[knotIndex], 'D') # Follow head's move

                    elif knotsCoord[headIndex][1] == knotsCoord[knotIndex][1]: # same col
                        if knotsCoord[headIndex][0] > knotsCoord[knotIndex][0]:
                            knotsCoord[knotIndex] = moveCoor(knotsCoord[knotIndex], 'R') # Follow head's move
                        else:
                            knotsCoord[knotIndex] = moveCoor(knotsCoord[knotIndex], 'L') # Follow head's move
                    else:
                        knotsCoord[knotIndex] = getTailCoord(knotsCoord[headIndex], knotsCoord[knotIndex]) # move diagonally

                h = parseCoord(knotsCoord[NB_KNOTS-1])
                if h not in lastKnotPos:
                    lastKnotPos.append(h) # register TailPos
            genTable(knotsCoord) # show sim /!\ dont work for input, only for the test one

print("Answer : ", len(lastKnotPos))
