tamanho = int(input())
valores = [int(x) for x in input().split()]

menor = valores[0]
posicao = 0

for i in range(1, tamanho):
    if valores[i] < menor:
        menor = valores[i]
        posicao = i

print("Menor valor:", menor)
print("Posicao:", posicao)
