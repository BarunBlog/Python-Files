T = int(input())

while T!=0:
    N,M = input().split()
    N,M = [int(N), int(M)]
    a,b = N,M
    if N==M or N==1 or M==1:
        print("Ari")
        T-=1
        continue

    i = 1
    a1 = 0
    r1 = 0
    while True:
        if a>b:
            u = int(a/b)
            if a%b==0:
                a=0
            elif u>=2:
                if b/(a%b)<2:
                     if i%2==1:
                         a1+=1
                     else:
                         r1+=1
                a = a - ((u-1)*b)

                #a = a-b
                #i+=1
            else:
                a = a - b
                #i+=1

        else:
            u = int(b/a)
            if b%a==0:
                b=0
            elif u>=2:
                if a/(b%a)<2:
                    if i%2==1:
                        a1+=1
                    else:
                        r1+=1
                b = b - ((u-1)*a)

                #b = b-a
                #i+=1
            else:
                b = b - a
                #i+=1

        if a==0 or b==0:
            break
        if a==1 or b==1:
            i+=1
            break
        i+=1
    #print(f"{a1} {r1}")
    if (a1==0 and r1==0) or a1==r1:
        if i%2==1:
            print("Ari")
        else:
            print("Rich")
    else:
        if a1>r1:
            print("Ari")
        else:
            print("Rich")

    T-=1
