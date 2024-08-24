class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        outputArr = []

        PrefMul = 1
        for num in nums:
            PrefMul *= num

            outputArr.append(PrefMul)

        postMul = 1
        for i in range(len(outputArr)-1, 0, -1):
            outputArr[i] = outputArr[i-1] * postMul
            postMul *= nums[i]

        outputArr[0] = postMul

        return outputArr
                


def main():
    li = [int(i) for i in input().split()]

    ob = Solution()
    print(ob.productExceptSelf(li))

if __name__ == "__main__":
    main()