f = open('input1.txt',"r")
input_list = []

for line in f:
    input_list.append(int(line.strip('\n')))
f.close()

length = len(input_list)
for i in range(length): 
    for j in range(i+1,length):
        for k in range(j+1,length):
            sum=input_list[i] + input_list[j] + input_list[k]
            if(sum==2020):
                print(sum)
                print(i)
                print(j)
                print(k)
                print(input_list[i])
                print(input_list[j])
                print(input_list[k])
                output = input_list[i]*input_list[j] * input_list[k]
                print(output)
        
