def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

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

        f1 = calcular_fatorial(n1)
        f2 = calcular_fatorial(n2)

        soma_fatoriais = f1 + f2
        print(soma_fatoriais)
