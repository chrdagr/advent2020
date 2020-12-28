lines = []
with open("input4.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!
 #   print(lines)

    length = len(lines)
    print(length)

    foundCID = False
    size = 0
    validCount = 0
    fullItem = []

    def checkItem(itm):
        itemL = len(itm)
    #    print(itemL)
        for i in range(itemL):
            subItem = itm[i].split(':')
            if (subItem[0] == 'cid'):
                return True
        return False

    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    def checkByr(itm):
        itemL = len(itm)
        for i in range(itemL):
            subItem = itm[i].split(':')
            if (subItem[0] == 'byr'):
                if(int(subItem[1])>= 1920 and int(subItem[1])<=2002):
                    return True
        return False


    #iyr (issue Year) - four digits; at least 1920 and at most 2002.
    def checkIyr(itm):
        itemL = len(itm)
        for i in range(itemL):
            subItem = itm[i].split(':')
            if (subItem[0] == 'iyr'):
                if(int(subItem[1])>= 2010 and int(subItem[1])<=2020):
                    return True
        return False

    #eyr (expiration Year) 
    def checkEyr(itm):
        itemL = len(itm)
        for i in range(itemL):
            subItem = itm[i].split(':')
            if (subItem[0] == 'eyr'):
                if(int(subItem[1])>= 2020 and int(subItem[1])<=2030):
                    return True
        return False

    #hgt (height) 
    def checkHgt(itm):
        itemL = len(itm)
        for i in range(itemL):
            subItem = itm[i].split(':')
            if (subItem[0] == 'hgt'):
                #subItem[1] = 184cm
                sil = len(subItem[1])
                if(subItem[1][-2:] == "cm"):
                    subItem[1] = subItem[1][:-2]
                    if (int(subItem[1]) >= 150 and int(subItem[1])<=193):
                        return True
                elif(subItem[1][-2:]== "in"):
                    subItem[1] = subItem[1][:-2]
                    if(int(subItem[1]) >=59 and int(subItem[1])<=76):
                        return True
        return False

    #hcl (hair color) 
    def checkHcl(itm):
        itemL = len(itm)
        for i in range(itemL):
            subItem = itm[i].split(':')
            if (subItem[0] == 'hcl'):
                #subItem[1] = 184cm
                sil = len(subItem[1])
                if (subItem[1][0] == '#' and sil == 7):
                    try:
                        int(subItem[1][1:],16)
                        return True
                    except:
                        pass
        return False

    #ecl (eye color) 
    def checkEcl(itm):
        itemL = len(itm)
        for i in range(itemL):
            subItem = itm[i].split(':')
            if (subItem[0] == 'ecl'):
                if (subItem[1] == "amb" or subItem[1]=="blu" or subItem[1]=="brn" or subItem[1]=="gry" or subItem[1]=="grn" or subItem[1]=="hzl" or subItem[1]=="oth"):
                    return True
        return False
    
    #pid () 
    def checkPid(itm):
        itemL = len(itm)
        for i in range(itemL):
            subItem = itm[i].split(':')
            if (subItem[0] == 'pid'):
                
                sil = len(subItem[1])
                if(sil == 9):
                    flag = True
                    for j in range(sil):
                        it = subItem[1][j]
                        if(not it.isdigit()):
                            flag = False
                    if (flag):
                        return True
                    else:
                        return False
        return False

    for i in range(length):
        if(lines[i] != ''):
            item = lines[i].split(' ')
            if(not foundCID):
                foundCID = checkItem(item)
            fullItem+=item
            size+=len(item)
        else: # found '' 
            #first examine the last passport
            if(size == 8):
                if(checkByr(fullItem) and checkEcl(fullItem) and checkEyr(fullItem) and checkHcl(fullItem) and checkHgt(fullItem) and checkIyr(fullItem) and checkPid(fullItem)):
                    validCount+=1
                    foundCID = False
                    size = 0
                    fullItem = []
                else:
                    foundCID = False
                    size = 0
                    fullItem = []
            elif(size == 7):
                if(not foundCID):
                    if(checkByr(fullItem) and checkEcl(fullItem) and checkEyr(fullItem) and checkHcl(fullItem) and checkHgt(fullItem) and checkIyr(fullItem) and checkPid(fullItem)):
                        validCount+=1
                        foundCID = False
                        size = 0
                        fullItem = []
                    else:
                        foundCID = False
                        size = 0
                        fullItem = []
                else:
                    foundCID = False
                    size = 0
                    fullItem = []
            else:
                foundCID = False
                size = 0
                fullItem = []
    
    print(validCount)
    
    if(size == 8):
        if(checkByr(fullItem) and checkEcl(fullItem) and checkEyr(fullItem) and checkHcl(fullItem) and checkHgt(fullItem) and checkIyr(fullItem) and checkPid(fullItem)):
            validCount+=1
            foundCID = False
            size = 0
    elif(size == 7):
        if(not foundCID):
            if(checkByr(fullItem) and checkEcl(fullItem) and checkEyr(fullItem) and checkHcl(fullItem) and checkHgt(fullItem) and checkIyr(fullItem) and checkPid(fullItem)):
                validCount+=1
                foundCID = False
                size = 0
        else:
            foundCID = False
            size = 0
    else:
        foundCID = False
        size = 0
    print(validCount)