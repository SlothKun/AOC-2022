import re

def moveDirectory(dirDepth, directory):
    dirDepth.pop() if directory == ".." else dirDepth.append(directory)
    return dirDepth

def listDirectory(fileInput, dirStructure, dirValidated, dirDepth):
    line = ""
    while '$' not in fileInput[0]:
        line = fileInput.pop(0).split()
        path = "".join([directory+"/" if directory != "/" else directory for directory in dirDepth])
        if line[0] == "dir":
            dirStructure[path+line[1]+"/"] = 0
            dirValidated[path+line[1]+"/"] = False
        elif line[0].isdigit():
            dirStructure[path] += int(line[0])
        if len(fileInput) == 0: # fail save in case there's no line left
            break
    return fileInput, dirStructure

def getDirectSubfolder(dirDepth, dirStructure):
    subfolder = []
    patternMatch = "^([a-zA-z]+/)"
    print("currentDepth : ", dirDepth)
    for dirPath in dirStructure:
        if dirDepth in dirPath and dirDepth != dirPath:
            print("dirPath : ", dirPath)
            patternRemove = f'^{dirDepth}'
            dirPath = re.sub(patternRemove, '', dirPath)
            dirPath = re.search(patternMatch, dirPath)
            print(dirPath)
            if dirPath:
                subfolder.append(dirPath.group(0))
    return list(set(subfolder))


def addSubfoldLength(dirDepth, dirStructure, dirValidated):
    # Get list of subfolder present
    subfolders = getDirectSubfolder(dirDepth, dirStructure)
    #print(subfolders)
    if len(subfolders) != 0:
        for subfolder in subfolders:
            subfolderPath = dirDepth+subfolder
            if not dirValidated[subfolderPath]:
                #print("Going to : ",subfolderPath)
                dirValidated, dirStructure = addSubfoldLength(subfolderPath, dirStructure, dirValidated)
            dirStructure[dirDepth] += dirStructure[subfolderPath]
        dirValidated[dirDepth] = True
    else:
        dirValidated[dirDepth] = True
    return dirValidated, dirStructure

def getAnswer(dirStructure):
    sizeSum = 0
    for size in dirStructure.values():
        if size <= 100000:
            sizeSum += size
    print("Answer : ", sizeSum)

dirStructure = {'/': 0}
dirValidated = {'/': False}
dirDepth = []
fileInput = [line.strip() for line in open("../input.txt").readlines()]

# first step, create the arborescence
while len(fileInput) != 0:
    instruction = fileInput.pop(0).split()
    if instruction[1] == "cd":
        dirDepth = moveDirectory(dirDepth, instruction[2])
    elif instruction[1] == "ls":
        fileInput, dirStructure = listDirectory(fileInput, dirStructure, dirValidated, dirDepth)


print(path for path in dirStructure)
for path in dirStructure:
    print(path)

print("----")
# Now that the arborescence is created, we need to add subfolder size to parent folders
dirDepth = '/' # Reset current path
dirValidated, dirStructure = addSubfoldLength(dirDepth, dirStructure, dirValidated)

print(dirStructure)
print(dirValidated)
# Get answer
getAnswer(dirStructure)
