# Leetcode: 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, num: list[int]) -> int:
        left = 0
        right = len(num) - 1

        if num[left] <= num[right]:
            return num[left]
        
        while left != right:
            mid = (left + right) // 2

            if num[left+1] < num[left]:
                return num[left+1]
            elif num[right-1] > num[right]:
                return num[right] 

            if num[left] < num[mid]:
                left = mid
            if num[mid] < num[right]:
                right =  mid
        
        return num[mid]


def main():
    li = [4,5,6,7]
    ob = Solution()

    print(ob.findMin(li))

if __name__ == "__main__":
    main()