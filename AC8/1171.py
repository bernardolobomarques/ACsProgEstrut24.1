qtd_vezes = int(input())

for _ in range(1, qtd_vezes):
    lista_x = []
    lista_cont = []
    for _ in range(qtd_vezes):
        x = int(input())
        for i in range(len(lista_x)):
            if lista_x[i] % x == 0:
                lista_x[i] += x
                lista_cont[i] += 1
        else:
            lista_x.append(x)
            lista_cont.append(1)

    # print(lista_x)
    
    lista_x.sort()

    for i in range(len(lista_x)):
        print(f"{int(lista_x[i]/lista_cont[i])} aparece {int(lista_cont[i])} vez(es)")