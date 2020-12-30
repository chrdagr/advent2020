import copy
lines = []

with open("input8.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!

length = len(lines)
accum = 0
count = {}
posList = []

def reRun(instructions):
    global accum
    accum = 0
    length = len(instructions)
    for i in range(length):
        count[i]=0
    i=0
    while i < length:
        op = instructions[i].split(' ',1)[0]
        val = instructions[i].split(' ',1)[1]
        if op == 'acc':
            count[i] += 1
            if(count[i]) > 1:
                return False
            i+=1
            accum += int(val)
        elif op == 'jmp':
           count[i] +=1
           if(count[i]) > 1:
               return False
           i+=int(val)
           
        elif op == 'nop':
            count[i] +=1
            if(count[i]) > 1:
               return False
            i+=1
    return True

def checkLine():
    if(count[i]) > 1:
        print(accum)
        print(posList)
        return False
    return True

for i in range(length):
    count[i] = 0

i=0
while i < length:
    op = lines[i].split(' ',1)[0]
    val = lines[i].split(' ',1)[1]
    if op == 'acc':
        count[i] += 1
        if(checkLine() == False):
            break
        i+=1
        accum += int(val)
    elif op == 'jmp':
        posList.append(i)
        count[i] +=1
        if(checkLine() == False):
            break
        i+=int(val)
    elif op == 'nop':
        posList.append(i)
        count[i] +=1
        if(checkLine() == False):
            break
        i+=1

print(len(posList))

for j in posList:
    if lines[j].split(' ',1)[0] == 'nop':
        tempList = copy.deepcopy(lines)
        tempItem = 'jmp '+lines[j].split(' ',1)[1]
        print(tempItem)
        tempList[j] = tempItem
    elif lines[j].split(' ',1)[0] == 'jmp':
        tempList = copy.deepcopy(lines)
        tempItem = 'nop '+lines[j].split(' ',1)[1]
        print(tempItem)

    tempList[j] = tempItem
    if(reRun(tempList) == True):
        print('accum is')
        print(accum)
        break
    else:
        tempList = []
