# Leetcode 875
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        start = 1
        end = max(piles)
        res = end

        while start <= end:
            mid = (start + end) // 2

            count_k = 0
            for banana in piles:
                count_k += math.ceil(banana / mid)

            if count_k <= h:
                res = min(res, mid)
                end = mid - 1
            elif count_k > h:
                start = mid + 1
        
        return res



def main():
    piles = [10]
    hours = 9

    ob = Solution()
    print(ob.minEatingSpeed(piles, hours))

if __name__ == "__main__":
    main()
