#!/usr/bin/env python3

def checkCycle(cycle, value):
    CYCLECHECK = [20, 60, 100, 140, 180, 220]
    return value*cycle if cycle in CYCLECHECK else 0



with open('../input.txt') as inputFile:
    cycleWait = {'addx':2, 'noop':1}
    signalSum = 0
    cycle = 0
    value = 1
    for line in inputFile:
        instruction = line.strip().split()
        for i in range(cycleWait[instruction[0]]):
            cycle += 1
            signalSum += checkCycle(cycle, value)
            if instruction[0] == 'addx' and i == cycleWait[instruction[0]]-1:
                value += int(instruction[1])

    print("Answer :", signalSum)
