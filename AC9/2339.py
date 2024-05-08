lista = input()
lista = lista.split()
n_competidores = int(lista[0])
n_folhas = int(lista[1])
n_folhas_comp = int(lista[2])

if (n_competidores*n_folhas_comp) <= n_folhas:
    print("S")
else:
    print("N")