# Leetcode 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        mySet = set()
        maxConSequence = 0
        counter = 0

        for num in nums:
            mySet.add(num)

        for num in mySet:
            
            if num - 1 not in mySet:
                # Which means num is the leftmost number in the sub sequence
                rightMost = num + 1
                counter = 1
                
                while rightMost in mySet:
                    rightMost += 1
                    counter += 1
                
                maxConSequence = max(counter, maxConSequence)
        
        return maxConSequence

                


def main():
    li = [int(i) for i in input().split()]

    ob = Solution()
    print("Maximum consecutive subsequence is: ", ob.longestConsecutive(li))

if __name__ == "__main__":
    main()