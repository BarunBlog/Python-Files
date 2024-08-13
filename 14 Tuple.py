tpl = (1, 2, 3, "Hello", 3.5, [4,5,6,10])
print(type(tpl)," ",tpl,"\n")
print(tpl[5]," ",tpl[-3])

for i in tpl:
    print(i, end=" ")
print("\n")

#converting tuple to list
li = list(tpl)
print(type(li),' ',li,"\n")

tpl2 = 1,2,3
print(type(tpl2)," ",tpl2)

a,b,c = tpl2
print(a," ",b," ",c)

t = (1)
print(type(t))

t1 = (1,)
print(type(t1))

'''
difference between tuple & list
Can not overwrite vales in tuple
'''

tpl3 = (1,2,3, [12,10], (14,15), 20)
print(tpl3)
