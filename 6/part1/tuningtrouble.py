with open("input.txt") as fileInput:
    datastream = fileInput.read()
    for i in range(4, len(datastream)):
        chunk = datastream[i-4:i]
        letterCount = [chunk.count(l) for l in set(chunk)]
        if letterCount.count(1) == 4:
            print("marker :", i)
            break