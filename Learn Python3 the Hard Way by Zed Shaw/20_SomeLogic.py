#vowel or not
ch = input('Take a character input: ')
if ch=='A' or ch=='a' or ch=='e' or ch =='E' or ch =='I' or ch=='i' or ch=='O' or ch=='o' or ch=='u' or ch=='U':
    print(f"character {ch} is vowel")
else:
    print(f"character {ch} is not vowel")

#Positive, Negative, Odd or Even
a = int(input('Take an integer input: '))
if a>=0 and a%2==0:
    print(f"The number {a} is Positive & Even")
elif a>0 and a%2!=0:
    print(f"The number {a} is Positive & Odd")
elif a<0 and 2-(a%2)==0:
    print(f"The number {a} is Negative & Even")
elif a<0 and 2-(a%2)!=0:
    print(f"The number {a} is Negative & Odd")

'''

-m%k = k-(m%k)

'''
