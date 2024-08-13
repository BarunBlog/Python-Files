li = []
print('Enter the length of list')
N = int(input())


for i in range(N):
    a = int(input())
    li.append(a)

for i in li:
    print(i, end=" ")
print()

## Taking input separated by space

li1 = []
li1 = list( map(int,input().split()) )

for i in li1:
    print(i, end=" ")
print()


'''
input()accepts a string from STDIN.

split()splits the string about whitespace character and returns
a list of strings.

map()passes each element of the 2nd argument to the first argument and
returns a map object

Finally list()converts the map to a list
'''
