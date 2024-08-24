
class Solution:

    def twoSum(self, numbers: list[int], target: int) -> list[list[int]]:

        i = 0
        j = len(numbers) - 1
        resArr = []

        while i < j:

            if numbers[i] + numbers[j] == target:
                resArr.append([0 - numbers[i] - numbers[j], numbers[i], numbers[j]])
                j -= 1

            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1

        return resArr


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        myHash = {}

        if nums[0] == 0 and nums[2] == 0:
            return [[0,0,0]]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] <= 0:
                twoSum = self.twoSum(nums[i+1:], 0 - nums[i])
                for li in twoSum:
                    myHash[tuple(li)] = li


        return myHash.values()

"""
    sample input 1:
    -1 0 1 2 -1 -4
 """
def main():
    li = [ int(i) for i in input().split()]

    ob = Solution()
    print(ob.threeSum(li))

if __name__ == "__main__":
    main()