# leetcode 42

class Solution:
    # O(n) time complexity and O(n) space complexity
    def trap(self, height: list[int]) -> int:
        leftMaxArr = []
        rightMaxArr = [0] * len(height)

        leftMax = 0
        for num in height:
            leftMaxArr.append(leftMax)
            leftMax = max(leftMax, num)

        rightMax = 0
        for i in range(len(height)-1, -1, -1):
            rightMaxArr[i] = rightMax
            rightMax = max(rightMax, height[i])

        print(leftMaxArr)
        print(rightMaxArr)

        total_water_unit = 0
        for i in range(len(height)):
            water_unit = min(leftMaxArr[i], rightMaxArr[i]) - height[i]

            if water_unit > 0:
                total_water_unit += min(leftMaxArr[i], rightMaxArr[i]) - height[i]
                  
        
        return total_water_unit
            
    def trap2(self, height: list[int]) -> int:
        maxLeft = 0
        maxRight = 0

        left = 0
        right = len(height) - 1

        total_water_unit = 0
        
        while left < right:
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])

            if maxLeft < maxRight:

                water_unit = maxLeft - height[left]

                if water_unit > 0:
                    total_water_unit += water_unit

                left += 1
            else:
                water_unit = maxRight - height[right]

                if water_unit > 0:
                    total_water_unit += water_unit

                right -= 1

        return total_water_unit

def main():
    # li = [int(i) for i in input().split()]

    # li = [4, 2, 0, 3, 2, 5, 2, 0, 1]

    li = [0,1,0,2,1,0,1,3,2,1,2,1]

    ob = Solution()
    print(ob.trap2(li))

if __name__ == "__main__":
    main()