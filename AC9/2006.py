resposta = int(input())
respostas = input()
respostas = respostas.split()
cont = 0
for i in range(len(respostas)):
    if int(respostas[i]) == resposta:
        cont += 1

print(cont)