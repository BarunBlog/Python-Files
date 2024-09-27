import math

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = math.ceil((start + end) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        
        return -1

def main():
    nums = [-1,0,3,5,9,12]
    target = 9

    ob = Solution()
    print(ob.search(nums, target))

if __name__ == "__main__":
    main()
