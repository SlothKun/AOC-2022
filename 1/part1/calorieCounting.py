#!/usr/bin/env python3

with open('../input.txt', 'r') as inputFile:
    currentCount = 0
    highestCount = 0
    for line in inputFile:
        if line.strip() != '':
            currentCount += int(line.strip('\n'))
        else:
            if currentCount > highestCount:
                highestCount = currentCount
            currentCount = 0
    print(f"The elf carrying the most calories has a total of {highestCount} Calories")
