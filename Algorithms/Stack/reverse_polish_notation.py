import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = ['+', '-', '/', '*']

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '/':
                    if a / b < 0:
                        stack.append(math.ceil(a / b))
                    else:
                        stack.append(math.floor(a / b))
                else:
                    stack.append(a * b)
            else:
                stack.append(int(token))

        return stack.pop()

def main():
    tokens = ["4", "-14", "/"]

    ob = Solution()
    print(ob.evalRPN(tokens))

if __name__ == "__main__":
    main()