lines = []
with open("input6ex.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!
   # print(lines)

length = len(lines)
print(length)

k=0
items = []
count = 0

for i in range(length):
    if(lines[i] != ''):
        k+=1
    else:
        tmp = ''.join(lines[(i-k):(i)])
        print(tmp)
        items.append("".join(set(tmp)))
        k = 0
        count+=len("".join(set(tmp)))
print(tmp)
tmp = ''.join(lines[(i-k+1):(i+1)])
items.append("".join(set(tmp)))
count+=len("".join(set(tmp)))
print(items)
print(count)