qtd = int(input())
cont = 0
for _ in range(qtd):
    lista = input()
    lista = lista.split()
    cont += int(lista[0])*int(lista[1])

print(cont)