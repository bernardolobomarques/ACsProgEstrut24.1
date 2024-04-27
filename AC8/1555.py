def rafael(x, y):
    return (3 * x) ** 2 + y ** 2

def beto(x, y):
    return 2 * (x ** 2) + (5 * y) ** 2

def carlos(x, y):
    return -100 * x + y ** 3

qtd_testes = int(input())

for _ in range(qtd_testes):
    valores = input().split()
    x = int(valores[0])
    y = int(valores[1])

    r = rafael(x, y)
    b = beto(x, y)
    c = carlos(x, y)

    if r > b:
        if r > c:
            print("Rafael ganhou")
        else:
            print("Carlos ganhou")
    elif b > c:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")
