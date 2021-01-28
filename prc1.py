
t = int(input())

while t!=0:

    n = int(input())
    if n<2020:
        print("NO")
        t = t-1
        continue

    x = round(n/2020)*2020
    y = round(n/2021)*2021

    #print(x,y)

    if n>=x and n<=y:
        print("YES")
    else:
        print("NO")

    t = t-1
