#!/usr/bin/env python3
import math

headCoord = [0, 0]
tailCoord = [0, 0]
allTailsPos = []


def getDistance(head, tail):
    return max(abs(head[0]-tail[0]), abs(head[1]-tail[1]))

def parseCoord(coor):
    return f"{coor[0]}-{coor[1]}"

def moveCoor(coor, side):
    if side == "L":
        coor[1] -= 1
    elif side == "R":
        coor[1] += 1
    elif side == "U":
        coor[0] += 1
    elif side == "D":
        coor[0] -= 1
    return coor

def getTailCoord(head, tail):
    moveNeeded = [math.copysign(1, head[0]-tail[0]), math.copysign(1, head[1]-tail[1])]
    return [tail[0]+moveNeeded[0], tail[1]+moveNeeded[1]]

with open("../input.txt") as inputFile:
    for move in inputFile:
        move = move.strip().split()
        for i in range(int(move[1])):
            headCoord = moveCoor(headCoord, move[0]) # Move head
            if getDistance(headCoord, tailCoord) > 1: # Check if head in perimeter, if so move
                if headCoord[0] == tailCoord[0] or headCoord[1] == tailCoord[1]:
                    tailCoord = moveCoor(tailCoord, move[0]) # Follow head's move
                else:
                    tailCoord = getTailCoord(headCoord, tailCoord) # move diagonally

            allTailsPos.append(parseCoord(tailCoord)) # register TailPos

print("Answer : ", len(set(allTailsPos)))
