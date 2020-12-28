lines = []
item = []
minmax = []
count = 0


with open("input2.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!

    length = len(lines)
    for i in range(length):
        item = lines[i].split(' ')
        minmax=item[0].split('-')
        min = int(minmax[0])
        max = int(minmax[1])
        letter = item[1][0]
        password = item[2]
        times = password.count(letter)
        if (times >= min and times <= max):
            count += 1


        #print(lines[i])

    #print(lines[0:60])
    print(count)