import math

memo = {}

def func(number):
    number = int(number)

    if number in memo:
        return memo[number]



    x = math.log(number, 2) # log(number) / log(2)

    n_lower = pow(2, math.floor(x))
    n_upper = pow(2, math.ceil(x))

    ans = 0

    if n_lower == n_upper:
        ans = int(x)
    if n_lower != n_upper:
        if number % 2 == 0:
            ans = 1 + func(number//2)
        else:
            value1 = 2 + func((number-1)//2)
            value2 = 2 + func((number+1)//2)
            ans = min(value1, value2)

    memo[number] = ans
    return memo[number]



def solution(n):
    number = int(n)

    x = math.log(number, 2) # log(number) / log(2)

    n_lower = pow(2, math.floor(x))
    n_upper = pow(2, math.ceil(x))

    global memo

    if n_lower == n_upper:
        return int(x)
    else:
        return func(number)




def main():
    n = input()
    min_op = solution(n)
    print(min_op)


if __name__ == "__main__":
    main()
