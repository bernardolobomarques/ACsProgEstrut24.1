cont = 0
x = int(input())
y = int(input())

if x > y:
    a = y
    b = x
else:
    a = x
    b = y

for i in range(a,b+1):
    if i%13 == 0:
        pass
    else:
        cont += i

print(cont)