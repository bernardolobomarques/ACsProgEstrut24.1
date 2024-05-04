entrada = int(input())
lista = []

for _ in range(entrada):
    num = int(input())
    lista.append(num)

contador = {}

for num in lista:
    if num in contador:
        contador[num] += 1
    else:
        contador[num] = 1

for i in sorted(contador.items()):
    print(f"{i[0]} aparece {i[1]} vez(es)")