lines = []
with open("input7.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!

length = len(lines)

rules = {}

def countBags(bagname):
    #shiny gold
    baglist = rules[bagname]
    if 'no other' in baglist:
        return 0
    howManyBagsIHave = 0
    howManyBagsMyBagsHave = 0
    for bag in baglist:
        bagtype = bag.split(' ',1)[1]
        howManyOfThatBag = int(bag.split(' ',1)[0])
        howManyBagsIHave += howManyOfThatBag
        howManyBagsMyBagsHave += howManyOfThatBag*countBags(bagtype)
    return howManyBagsIHave + howManyBagsMyBagsHave
    
for i in range(length):
    #print(lines[i])
    tmp = lines[i].split(' contain')[0].rsplit(' ',1)[0]
    tmp2 = lines[i].split(' contain ')[1].strip('.')
    tmp3 = tmp2.split(',')
    for j in range(len(tmp3)):
        tmp3[j]=tmp3[j].strip().rsplit(' ',1)[0]
    
    rules[tmp] = tmp3
        
bagsNr = countBags('shiny gold')
print(bagsNr)