with open("input.txt") as fileInput:
    datastream = fileInput.read()
    for i in range(14, len(datastream)):
        chunk = datastream[i-14:i]
        letterCount = [chunk.count(l) for l in set(chunk)]
        if letterCount.count(1) == 14:
            print("marker :", i)
            break