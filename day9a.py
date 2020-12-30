lines = []
from collections import deque

with open("input9.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!

preamble = deque()
for i in range(25):
    preamble.append(lines[i])
print('preamble is ')
print(preamble)

def isSum(number):
    for i in range(len(preamble)):
        for j in range(i+1,len(preamble)):
            if (int(preamble[i]) + int(preamble[j]) == number):
                print('for number '+str(number)+' i is '+str(i)+' preamble is '+preamble[i]+' j is '+str(j)+' preamble is '+preamble[j])
                return True
    return False

for i in range(25,len(lines)):
    #find the first number that is not the sum of two of the 25 numbers before it.
    tNr = int(lines[i])
    if (isSum(tNr) != True):
        print('Number is '+str(tNr)+' i is '+str(i))
        break
    else:
        #update preamble
        preamble.popleft()
        preamble.append(lines[i])