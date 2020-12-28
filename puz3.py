lines = []
with open("input3.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!
    length = len(lines[0]) #31
   
    print(length)
    size = len(lines)
   # posX = 0
    #posY = 0
    #countTrees = 0

    def slope(xIncr,yIncr):
        posX = 0
        posY = 0
        countTrees = 0
        while posX <= size-1:
            if(posY+yIncr > length-1):
                posY=posY+yIncr-length
                posX+=xIncr
            else:
                posY+=yIncr
                posX+=xIncr
            if(posX <= (size-1) and lines[posX][posY] == '#'):
                countTrees+=1
        return countTrees

    count = slope(1,3) * slope(1,1) * slope(1,5) * slope(1,7) * slope(2,1)
    print(count)