name = 'Barun Bhattacharjee'
for letter in name:
    print(letter, end=" ")
print("\n\n")


# print elements of list using for loop

li = ["computer", "mobile", "cell phone", "laptop"]
for i in li:
    print(i)
print("\n\n")


li = ["computer", "mobile", "cell phone", "laptop"]
for i in li[:2]:
    print(i)
print("\n\n")



for i in li:
    print(len(i))
print("\n")

for i in range(1,10):
    if i==6:
        break
    print(i, end=" ")
print("\n")

for i in range(10,50,5):
    print(i, end=" ")
print("\n")


for i in range(50,10,-5):
    print(i, end=" ")
print("\n")



## printing N number of prime numbers
    
N = int(input())

for i in range(2,N+1):
    ck=0
    for j in range(2,i):
        if i%j==0:
            i+=1
            j=1
            ck=1
            continue
        
    if ck==0:
        print(i, end=" ")
print()

