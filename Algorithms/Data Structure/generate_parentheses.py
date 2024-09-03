# Leetcode 22

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []

        def generate_with_rec(l: int, r: int, resStr: str) -> str:

            print(f"l: {l}, r: {r}, resStr: {resStr}")

            if l == n and r == n:
                stack.append(resStr)
                return

            if l > r:
                if l <= n:
                    generate_with_rec(l=l+1, r=r, resStr=resStr + "(")
                if r <= n:
                    generate_with_rec(l=l, r=r+1, resStr=resStr + ")")
            
            if l == r and l <= n:
                generate_with_rec(l=l+1, r=r, resStr=resStr + "(")
                
        
        generate_with_rec(0, 0, "")

        return stack



def main():
    ob = Solution()

    print(ob.generateParenthesis(n=3))

if __name__ == "__main__":
    main()