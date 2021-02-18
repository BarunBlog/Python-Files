
if __name__ == "__main__":
    str = input()

    len = len(str)
    str2 = ""
    for i in range(len):
        if str[i].islower():
            str2 = str2 + str[i].upper()
        elif str[i].isupper():
            str2 = str2 + str[i].lower()
        else:
            str2 = str2 + str[i]

    print(str2)
