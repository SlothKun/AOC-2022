#!/usr/bin/env python3

def checkPairs(pairs):
    pair1 = [int(nb) for nb in pairs[0].split('-')]
    pair2 = [int(nb) for nb in pairs[1].split('-')]
    if pair1[0] <= pair2[0] <= pair2[1] <= pair1[1] or \
       pair2[0] <= pair1[0] <= pair1[1] <= pair2[1]:
        return 1
    else:
        return 0

with open('../input.txt', 'r') as fileInput:
    validPairCount = 0
    for line in fileInput:
        pairs = line.strip().split(',')
        validPairCount += checkPairs(pairs)
    print(validPairCount)
