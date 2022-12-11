#!/usr/bin/env python3
import math

# Functions
def testItem(item, testNb):
    return True if (item % testNb) == 0 else False

def doMath(item, opSign, nb):
    nb = int(nb) if nb != 'old' else item
    return item+nb if opSign == "+" else item*nb # can only be + or *

# Vars
monkeys = {}

# Parse input
with open("../input.txt") as inputFile:
    dataStage = 0
    cMonkeyNb = -1
    for line in inputFile:
        line = line.strip().split()
        if len(line) == 0:
            dataStage = -1
        elif dataStage == 0: # Create monkey entry
            cMonkeyNb = int(line[1][:-1])
            monkeys[cMonkeyNb] = {'inspected':0}
        elif dataStage == 1: # Get currently holded items
            monkeys[cMonkeyNb]['items'] = [int(item.strip(',')) for item in line[2:]]
        elif dataStage == 2: # Get his operation (First bit will always be 'old', so don't add it)
            monkeys[cMonkeyNb]['opSign'] = line[-2]
            monkeys[cMonkeyNb]['opNb'] = line[-1]
        elif dataStage == 3: # Get his test
            monkeys[cMonkeyNb]['test'] = int(line[-1])
        elif dataStage == 4: # monkey if true
            monkeys[cMonkeyNb][True] = int(line[-1])
        elif dataStage == 5: # mokey if false
            monkeys[cMonkeyNb][False] = int(line[-1])
        dataStage += 1
    print(monkeys)

# Least Common Multiplier
# By multiplying every divisor together, we get a number that we can use for modulus
# we're guaranteed that this will work become it'll be common to every divisors used
LCM = 1
for nb in monkeys.values():
    LCM *= nb['test']

# Run the simulation for 20 rounds
for i in range(10000):
    for mNb in monkeys.keys():
        while len(monkeys[mNb]['items']) != 0:
            item = monkeys[mNb]['items'].pop(0)
            monkeys[mNb]['inspected'] += 1
            # Op
            item = doMath(item, monkeys[mNb]['opSign'], monkeys[mNb]['opNb'])
            item %= LCM
            # Test
            testResult = testItem(item, monkeys[mNb]['test'])
            # Action
            target = monkeys[mNb][testResult]
            monkeys[target]['items'].append(item)

# Get answer
inspectList = sorted([data['inspected'] for data in monkeys.values()])
print(inspectList)
print(inspectList[-1], inspectList[-2])
print("Monkey Business : ", inspectList[-1] * inspectList[-2])
