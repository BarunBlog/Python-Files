# Leetcode: 153. Find Minimum in Rotated Sorted Array
class Solution:
    def search(self, num: list[int], target: int) -> int:
        left = 0
        right = len(num) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if num[mid] == target:
                return mid
            
            # check if the left half is sorted
            if num[left] <= num[mid]:
                if num[left] <= target < num[mid]:
                    right = mid - 1 # target is in the left half
                else:
                    left = mid + 1 # target is in the right half
            # check if the right half is sorted
            else:
                if num[mid] < target <= num[right]:
                    left = mid + 1 # target is in the right half
                else:
                    right = mid - 1 # target is in the left half
        
        return -1


def main():
    li = [4,5,6,7,0,1,2]
    target = 0
    ob = Solution()

    print(ob.search(li, target))

if __name__ == "__main__":
    main()