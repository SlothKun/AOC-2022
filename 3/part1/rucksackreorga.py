#!/usr/bin/env python3

def findSharedItem(compA, compB):
    for itemA in compA:
        for itemB in compB:
            if itemA == itemB:
                print(itemA, " -> ", ord(itemA)-96 if itemA.islower() else ord(itemA)-38)
                return ord(itemA)-96 if itemA.islower() else ord(itemA)-38

with open("../input.txt") as inputFile:
    prioritySum = 0
    for rucksack in inputFile:
        rucksack = rucksack.strip()
        compA, compB = rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):]
        prioritySum += findSharedItem(compA, compB)
    print(f"Total sum : {prioritySum}")
