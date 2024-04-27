def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

n_testes = int(input())

for i in range(n_testes):
    num = input()
    num = num.split()
    for i in range(len(num)):
        num[i] = int(num[i])

    num.sort()
    cont = mdc(num[0], num[1])

    print(cont)
