# O(nlog) solution
class Solution:
    def binarySearch(self, numbers: list[int], start: int, end: int, number: int) -> int:

        while start <= end:
            mid = int((start + end) / 2)

            if numbers[mid] == number:
                return mid

            if numbers[mid] < number:
                start = mid + 1

            if numbers[mid] > number:
                end = mid - 1

        return -1

        

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        for i in range(len(numbers)):
            firstNum = numbers[i]
            start = i + 1
            end = len(numbers) - 1

            secondNumPosition = self.binarySearch(numbers, start, end, target - firstNum)

            if secondNumPosition != -1:
                return [i+1, secondNumPosition+1]

# O(n) Solution
class Solution2:

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        i = 0
        j = len(numbers) - 1
        while numbers[i] + numbers[j] != target:

            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
        
        return [i+1, j+1]

def main():
    numbers = [int(i) for i in input().split()]
    target = int(input())

    ob = Solution()
    print(ob.twoSum(numbers, target))

if __name__ == "__main__":
    main()