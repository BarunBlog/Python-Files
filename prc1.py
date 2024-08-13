
def main():

    str = input()
    ln = len(str)

    counter = [0] * 26

    for chr in str:
        counter[ ord(chr) - 97 ] += 1

    unique_num = set()
    for n in counter:
        if n!=0:
            unique_num.add(n)

    if len(unique_num) == 1:
        print('YES')
    elif len(unique_num) > 2:
        print('NO')
    else:
        first = list(unique_num)[0]
        second = list(unique_num)[1]

        if abs(first - second) > 1:
            print('NO')

        else:
            for occ in counter:








if __name__ == '__main__':
    main()
