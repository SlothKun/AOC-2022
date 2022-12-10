#!/usr/bin/env python3

from re import match


headCoord = [0, 0]
tailCoord = [0, 0]
allTailsPos = []

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

with open("../input.txt.example") as inputFile:
    for move in inputFile:
        move = move.strip().split()
        for i in range(int(move[1])):
            # Move head first
            headCoord = moveCoor(headCoord, move[0])
            # Verify Distance
            # if head in range 1 -> dont move
            # elif head not in range 1 but same row or col -> move to H
            # else not in range and not same row -> move to H diagonally

            # register pos in format x-y in allTailsPos
            allTailsPos.append(parseCoord(tailCoord))

print("Answer : ", len(set(allTailsPos)))
