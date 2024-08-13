memo = []

def lcs(i, j, str1, str2):
        if i == len(str1) or j == len(str2):
            return 0;
        if memo[i][j] != -1:
            return memo[i][j];
        ans = 0
        if str1[i] == str2[j]:
            ans = 1 + lcs(i+1, j+1, str1, str2)
        else:
            value1 = lcs(i+1, j, str1, str2)
            value2 = lcs(i, j+1, str1, str2)

            ans = max(value1, value2)

        memo[i][j] = ans
        return memo[i][j]



def main():
    global memo
    memo = [[-1]*1001 for _ in range(1001)]

    str1 = input()
    str2 = input()
    lcs_len = lcs(0, 0, str1, str2)
    print(lcs_len)

if __name__ == "__main__":
    main()
