# Leetcode 853

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        pair = [[position, speed] for position, speed in zip(position, speed) ]

        stack = []
        for position, speed in sorted(pair)[::-1]: # Reverse sorted order by position
            time = (target - position) / speed
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)


def main():
    ob = Solution()

    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]

    print(ob.carFleet(target, position, speed))

if __name__ == "__main__":
    main()