lines = []
with open("input9.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!

k=0

def calcSum(sumN,k):
    maxN = sumN
    minN = sumN

    for i in range(k+1,len(lines)):
        if (int(lines[i]) > maxN):
            maxN = int(lines[i])
        if (int(lines[i]) < minN):
            minN = int(lines[i])

        sumN+=int(lines[i])
        if(sumN == 90433990):
            print('reached 90433990. Min is '+str(minN)+' max is '+str(maxN))
            return(minN+maxN)
        elif sumN > 90433990:
            return None

while k < len(lines):
    res = calcSum(int(lines[k]),k)
    if res is None:
        k+=1
    else:
        print('result is '+str(res))
        break