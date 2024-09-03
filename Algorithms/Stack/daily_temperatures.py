# Leetcode 739
# Monotonicly Decreasing Stack

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp = stack.pop()
                result[ temp[1] ] = i - temp[1]

            stack.append((temperatures[i], i))
        
        return result
                    


def main():
    ob = Solution()

    temperatures = [73,74,75,71,69,72,76,73]

    print(ob.dailyTemperatures(temperatures=temperatures))

if __name__ == "__main__":
    main()