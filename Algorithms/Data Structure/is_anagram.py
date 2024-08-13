
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}

        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            hashMap1[s[i]] = hashMap1.get(s[i], 0) + 1
            hashMap2[t[i]] = hashMap2.get(t[i], 0) + 1

        for key in hashMap1:
            if hashMap1[key] != hashMap2.get(key, 0):
                return False
        return True

def main():
    str1 = input()
    str2 = input()

    sl = Solution()
    
    if sl.isAnagram(str1, str2):
        print("The strings are anagram to each other")
    else:
        print("The strings are not anagram to each other")



if __name__ == "__main__":
    main()