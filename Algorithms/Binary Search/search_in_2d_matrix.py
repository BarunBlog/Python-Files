# Leetcode 74

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])

        start = 0
        end = row * col - 1

        while start <= end:
            mid = (start + end) // 2

            if matrix[mid // col][mid % col] == target:
                return True
            elif matrix[mid // col][mid % col] < target:
                start = mid + 1
            elif matrix[mid // col][mid % col] > target:
                end = mid - 1

        return False

def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 2

    ob = Solution()
    print(ob.searchMatrix(matrix, target))

if __name__ == "__main__":
    main()
    