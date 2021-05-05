memo = []

def func(i, li):
    if(memo[i] != -1):
        return memo[i]

    ans = 0
    for j in range(i+1, len(li)):
        if(li[j] > li[i]):
            ans = max(ans, func(j, li))

    memo[i] = ans + 1
    return memo[i]

def findLIS(li):
    ans = 0
    for i in range(0, len(li)):
        ans = max(ans, func(i, li))

    return ans

def main():
    T = int(input())

    while T != 0:
        N = int(input())
        li = list(map(int, input().split()))

        global memo
        memo = [-1] * N

        lis = findLIS(li)
        print(lis)

        T = T - 1




if __name__ == '__main__':
    main()
