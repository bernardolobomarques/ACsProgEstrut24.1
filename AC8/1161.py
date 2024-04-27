while True:
    try:
        valores = input()
    except EOFError:
        break
    
    if valores.upper() == "EOF":
        break
    else:
        valores = valores.split()
        n1 = int(valores[0])
        n2 = int(valores[1])

        f1 = 1
        f2 = 1

        for i in range(n1, 1, -1):
            f1 *= i

        for i in range(n2, 1, -1):
            f2 *= i

        soma_fatoriais = f1 + f2
        print(soma_fatoriais)
