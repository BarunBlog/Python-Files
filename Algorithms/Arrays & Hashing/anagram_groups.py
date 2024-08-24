# Leetcode 49

class Solution:
    # Complexity O(m * n log n)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        resultList = []
        hashMap = {}

        for str in strs:
            
            sortedStr = ''.join(sorted(str))

            hashMap[sortedStr] = hashMap.get(sortedStr, []) + [str]

        
        for key in hashMap:
            resultList.append(hashMap[key])

        return resultList
    

    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:

        hashMap = {}

        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord("a")] += 1

            hashMap[tuple(count)] = hashMap.get(tuple(count), []) + [str]

        return hashMap.values()



def main():
    strs = input().split()

    sl = Solution()

    print(sl.groupAnagrams2(strs))

if __name__ == "__main__":
    main()