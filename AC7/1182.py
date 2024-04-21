coluna = int(input())
operacao = input().upper()

matriz = []
for _ in range(12):
    linha = []
    for _ in range(12):
        temp = float(input())
        linha.append(temp)
    matriz.append(linha)



soma = 0

for i in range(12):
    soma += matriz[i][coluna]

if operacao == 'M':
    media = soma / 12
    print(f'{media:.1f}')
elif operacao == 'S':
    print(f'{soma:.1f}')
