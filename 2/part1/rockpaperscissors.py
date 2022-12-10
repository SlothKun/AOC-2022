#!/usr/bin/env python3

with open("../input.txt") as inputFile:
    scoreSheet = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    totalScore = 0

    for line in inputFile:
        play = line.strip('\n')
        totalScore += scoreSheet[play]

    print(f'totalScore : {totalScore}')
