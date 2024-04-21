cont = 0
for _ in range(5):
    temp = int(input())
    if temp%2 == 0:
        cont += 1

print(f"{cont} valores pares")