#!/usr/bin/env python3

with open('../input.txt') as inputFile:
    cycleWait = {'addx':2, 'noop':1}
    cycle = 0
    value = 1
    crtLine = ''
    crt = []
    for line in inputFile:
        instruction = line.strip().split()
        for i in range(cycleWait[instruction[0]]):
            cycle += 1

            # draw pixel
            patternCoord = [value-1, value, value+1]
            if cycle-1 in patternCoord:
                crtLine += '#'
            else:
                crtLine += '.'

            # next line
            if cycle%40 == 0:
                crt.append(crtLine)
                crtLine = ''
                cycle = 0

            # Update value
            if instruction[0] == 'addx' and i == cycleWait[instruction[0]]-1:
                value += int(instruction[1])


    for crtLine in crt:
        print(crtLine)
