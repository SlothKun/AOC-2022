#!/usr/bin/env python3

with open('../input.txt', 'r') as inputFile:
    topThreeCount = [0,0,0]
    currentCount = 0
    for line in inputFile:
        if line.strip() != '':
            currentCount += int(line.strip('\n'))
        else:
            if currentCount > topThreeCount[0]:
                topThreeCount[2] = topThreeCount[1]
                topThreeCount[1] = topThreeCount[0]
                topThreeCount[0] = currentCount
            elif currentCount > topThreeCount[1]:
                topThreeCount[2] = topThreeCount[1]
                topThreeCount[1] = currentCount
            elif currentCount > topThreeCount[2]:
                topThreeCount[2] = currentCount
            currentCount = 0

    print(f"{topThreeCount[0]} - {topThreeCount[1]} - {topThreeCount[2]}")
    print(f"The top three elves carrying the most calories has a total of {topThreeCount[0] + topThreeCount[1] + topThreeCount[2]} Calories")
