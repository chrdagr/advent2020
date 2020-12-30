lines = []
with open("input7.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!

length = len(lines)
#print(lines)
count = 0
rules = {}
init_bags = []
bags = []

def checkBags(bag):
    for key, values in rules.items():
        #print(values)
        #print('bag is '+bag)
        for k in range(len(values)):
            if(bag in values[k]):
                
                if(key.rsplit(' ', 1)[0] not in bags):
                    bags.append(key.rsplit(' ', 1)[0])
                    
                    #print('key is '+key)
                    #print(bags)
                    #checkBags(key)

        #print values

for i in range(length):
    #print(lines[i])
    tmp = lines[i].split(' contain')[0]
    tmp2 = lines[i].split(' contain ')[1].translate(None, '0123456789').strip('.')
    tmp3 = tmp2.split(',')
    for j in range(len(tmp3)):
        tmp3[j]=tmp3[j].strip()
    
    rules[tmp] = tmp3
    if ("shiny gold" in tmp2):
        bags.append(tmp.rsplit(' ',1)[0])
        
#print(bags)
#print(rules)
#print(count)
for b in bags:
   checkBags(b)

count = len(init_bags) + len(bags)
#print(init_bags)
print ('*****')
print(bags)
print(count)
