def substring(str):
    ln = len(str)

    StuartCount = 0
    KevinCount = 0

    for i in range(0,ln):
        for j in range(1,ln-i+1):
            print(str[i:i+j])
        print()



if __name__ == '__main__':
    str = input()
    substring(str)
