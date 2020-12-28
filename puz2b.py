lines = []
item = []
pos = []
count = 0


with open("input2.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!

    length = len(lines)
    for i in range(length):
        item = lines[i].split(' ')
        pos=item[0].split('-')
        pos1 = int(pos[0])
        pos2 = int(pos[1])
        letter = item[1][0]
        password = item[2]
        print(password)
        print(pos1)
        print(pos2)
        print(letter)
        
        if (len(password) >= pos1 and len(password) >= pos2):
            if ((password[pos1-1] == letter and password[pos2-1] != letter) or (password[pos1-1] != letter and password[pos2-1] == letter)):
                count += 1
                #print("true")
                #print(password)


        #print(lines[i])

    #print(lines[0:60])
    print(count)