'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

'''


memo = []

def lcs(i, j, str1, str2):

    if i == len(str1) and j == len(str2):
        return 0;
    if memo[i][j] != -1:
        return memo[i][j];
    if i == len(str1):
        return len(str2) - j
    if j == len(str2):
        return len(str1) - i

    ans = 0
    if str1[i] == str2[j]:
        ans = lcs(i+1, j+1, str1, str2)
    else:
        insert = 1 + lcs(i, j+1, str1, str2)
        delete = 1 + lcs(i+1, j, str1, str2)
        replace = 1 + lcs(i+1, j+1, str1, str2)

        ans = min(insert, delete, replace)
    memo[i][j] = ans
    return memo[i][j]



def main():
    global memo
    memo = [[-1]*501 for _ in range(501)]

    str1 = input()
    str2 = input()
    lcs_len = lcs(0, 0, str1, str2)
    print(lcs_len)

if __name__ == "__main__":
    main()
