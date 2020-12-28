lines = []
with open("input6.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!

length = len(lines)

k=0
items = []
count = 0

for i in range(length):
    if(lines[i] != ''):
        k+=1
    else:
        tmp = ''.join(lines[(i-k):(i)])
        tmp2 = "".join(set(tmp))
        items.append(tmp2)
        for char in tmp2:
            if (tmp.count(char) == k):
                count+=1
        k = 0

tmp = ''.join(lines[(i-k+1):(i+1)])
tmp2 = "".join(set(tmp))
items.append(tmp2)
for char in tmp2:
    if (tmp.count(char) == k):
        count+=1
print(count)