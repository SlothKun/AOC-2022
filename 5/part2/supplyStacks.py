#!/usr/bin/env python3
import re

def parseInstructions(instruction):
    order = re.findall("[0-9]+", instruction)
    return [int(i) for i in order]

def applyInstructions(order, stacks):
    boxes = stacks[order[1]][-order[0]:]
    stacks[order[1]] = stacks[order[1]][:-order[0]]
    stacks[order[2]] = stacks[order[2]] + boxes
    return stacks

def getAnswer(stacks):
    return "".join(s[-1] for s in stacks.values())

with open("../input.txt", 'r') as inputFile:
    tableEnd = 0
    stacks = {}
    for line in inputFile:
        if line == "\n" or line.replace(' ', '').strip().isdigit():
            tableEnd += 1
        elif tableEnd == 0:
            # Parse the initial stack
            currentCol = 1
            while len(line) != 0:
                colContent = line[:3]
                if currentCol not in stacks:
                    stacks[currentCol] = ""
                if colContent[0] == '[':
                    stacks[currentCol] = colContent.strip('[]') + stacks[currentCol]
                currentCol += 1
                line = line[4:]
        elif tableEnd == 2:
            order = parseInstructions(line)
            stacks = applyInstructions(order, stacks)
            print(stacks)

    print(getAnswer(stacks))
