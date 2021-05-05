def is_consecutive_number(str):
    str_len = len(str)
    temp_str = ""
    ck = False
    for i in range(int(str_len/2)):
        temp_str = temp_str + f"{str[i]}"
        temp_len = len(temp_str)
        temp_int = int(temp_str)
        one_digit_added = False

        #for j in range(i+1, str_len, temp_len):
        j = i + 1
        while(j<str_len):
            temp_str2 = ""

            for k in range(j, j+temp_len):
                temp_str2 = temp_str2 + str[k]

            temp_int2 = int(temp_str2)
            print("Temp int ", temp_int)
            print("temp_int2 ", temp_int2, "\n")

            if temp_int+1 == temp_int2:
                temp_int = temp_int2
                one_digit_added = False
                if j==str_len-temp_len:
                    ck = True
                    break
            else:
                if j+temp_len+1 <= str_len and one_digit_added==False:
                    j = j - temp_len - 1
                    temp_len = temp_len + 1
                    #print(temp_len)
                    one_digit_added = True
                    print(one_digit_added)
                else:
                    break
            j = j + temp_len

        if ck == True:
            break

    return ck

str = input()
print(is_consecutive_number(str))
