fr = open("prc_input1.txt","r")
fw = open("prc_output1.txt","w")
text = fr.readline()
print(text)

n = int(text)

text = fr.readline()
li = list(text)
li2 = []

#print((li[1]));

for i in range(0,len(li)):
    if li[i]>='0' and li[i]<='9':
        li2.append(int(li[i]))




sum = 0
avg = 0
for i in range(0,len(li2)):
    sum += li2[i]
avg = sum/n

print("Sum is ", sum)
fw.write(f"Sum is {sum}\n")
print("Average is ",avg);
fw.write(f"Average is {avg}\n")
