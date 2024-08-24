class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        hashMap = {}

        for i in range(len(nums)):

            if target - nums[i] in hashMap:
                return [hashMap.get(target - nums[i]), i]

            hashMap[nums[i]] = i


def main():
    nums = [int(num) for num in input().split()]
    target = int(input())

    ob = Solution()
    print(ob.twoSum(nums, target))

if __name__ == "__main__":
    main()