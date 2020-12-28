lines = []
seats = []

with open("input5.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!

    length = len(lines)

    for i in range(length):
        seatF=0
        seatB=127
        seatRow = 0
        seatR = 7
        seatL = 0
        seatCol = 0
        number = 0

        for k in range(0,6):
            if(lines[i][k] == 'F'):
                seatB = seatF + (seatB - seatF) // 2
            elif(lines[i][k] == 'B'):
                seatF = seatB - ((seatB-seatF) // 2)

        if(lines[i][6] == 'F'):
            seatRow = seatF
        elif(lines[i][6] == 'B'):
            seatRow = seatB

        for j in range(7,9):
            if(lines[i][j] == 'L'):
                seatR = seatL + ((seatR - seatL) // 2)
            elif(lines[i][j] == 'R'):
                seatL = seatR - ((seatR - seatL) // 2)

        if(lines[i][9] == 'R'):
            seatCol = seatR
        elif(lines[i][9] == 'L'):
            seatCol = seatL
        
        number = seatRow*8+seatCol

        seats.append(number)

    numLength = len(seats)
    maxN = max(seats)
    print(maxN)

    #part 2
    seats.sort()
    for l in range(1,numLength-1):
        if ((seats[l] != seats[l-1] + 1)):
            print("This seat is missing "+str(seats[l-1] +1))