'''res = 0
for i in range(1,11):
    res = i+res
print(res)'''


x= int(input("enter a number"))
res = 0
for i in range(len(str(x))):
    rem = x%10
    res = res*10 + rem
    x = x//10
print(res)
