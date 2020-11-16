T = int(input())

while T!=0:
    N,M = input().split()
    N,M = [int(N), int(M)]
    if N==M:
        print("Ari")
        T-=1
        continue
    a,b = N,M

    #dictionary
    matches = {}
    i=1
    while True:
        if N%M<N:
            N = N%M
        else:
            M = M%N

        str = f"{N}{M}"
        if i%2!=0:
            matches[str] = 1
            winner = 1
        else:
            matches[str] = 0
            winner = 0

        #print(f"{N} {M}")

        if N==0 or M==0:
            break
        i+=1

    '''if i%2==1:
        print(f"w Ari {winner}")
    else:
        print(f"w Rich {winner}")
    for N1, M1 in list(matches.items()):
        print(f"{N1} is {M1}")'''

    i = 1
    while True:
        x,y = a,b
        if a%b<a:
            x = a%b
            u = int(a/b)
        else:
            y = b%a
            u = int(b/a)
        ck=0
        str = f"{x}{y}"
        try:
            if i%2 == matches[str] and i%2 == winner:
                ck=1
                a,b = x,y
            else:
                if a>b:
                    if u>=2:
                        a = a - ((u-1)*b)
                        a = a-b
                        i+=2
                    else:
                        ck=1
                        a,b = x,y
                else:
                    if u>=2:
                        b = b - ((u-1)*a)
                        b = b-a
                        i+=2
                    else:
                        ck=1
                        a,b = x,y
        except KeyError:
            if a>b:
                if u>=2:
                    a = a - ((u-1)*b)
                    a = a-b
                    i+=2
                else:
                    ck=1
                    a,b = x,y
            else:
                if u>=2:
                    b = b - ((u-1)*a)
                    b = b-a
                    i+=2
                else:
                    ck=1
                    a,b = x,y
        #print(f"{a} {b}")
        if a==0 or b==0:
            break
        if ck==1:
            i+=1

    if i%2==1:
        print("Ari")
    else:
        print("Rich")

    T-=1
