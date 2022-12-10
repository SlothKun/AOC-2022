#!/usr/bin/env python3

def findSharedItem(group):
    # find the common letter between the 3 strings and return its priority
    badge = ''.join(set(group[0]) & set(group[1]) & set(group[2]))
    return ord(badge)-96 if badge.islower() else ord(badge)-38

with open("../input.txt") as inputFile:
    group = []
    prioritySum = 0
    for rucksack in inputFile:
        group.append(rucksack.strip())
        if len(group) == 3:
            prioritySum += findSharedItem(group)
            group = []
    print(f"Total sum : {prioritySum}")
