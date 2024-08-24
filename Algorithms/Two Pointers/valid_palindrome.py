# Leetcode 125. Valid Palindrome

class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        
        plainStr = ''.join(char for char in s if char.isalnum()).lower()

        i = 0
        j = len(plainStr) - 1

        print(plainStr)

        while i <= j:

            if plainStr[i] != plainStr[j]:
                return False

            i += 1
            j -= 1

        return True


def main():
    str = input()

    ob = Solution()

    print(ob.isPalindrome(str))

if __name__ == "__main__":
    main()