def ex_1000():
    print("Hello World!")

def ex_1001():
    a = int(input())
    b = int(input())
    x = a + b
    print("X =", x)

def ex_1010():
    dados1 = input()
    dados2 = input()

    dados1 = dados1.split(" ")
    dados2 = dados2.split(" ")
    preco = int(dados1[1]) * float(dados1[2]) + int(dados2[1]) * float(dados2[2])
    print(f"VALOR A PAGAR: R$ {preco:.2f}")

# ex_1010()
    
def ex_1013():
    dados = input()

    dados = dados.split(" ")
    dados[0] = int(dados[0])
    dados[1] = int(dados[1])
    dados[2] = int(dados[2])

    if dados[0]>dados[1] and dados[0] > dados[2]:
        print(dados[0], "eh o maior")
    elif dados[1]>dados[0] and dados[1]>dados[2]:
        print(dados[1], "eh o maior")
    elif dados[2]>dados[0] and dados[2]>dados[1]:
        print(dados[2], "eh o maior")

# ex_1013()
        
def ex_1017():
    a = input()
    a = a.split(" ")
    a[0] = float(a[0])
    a[1] = float(a[1])
    b = input()
    b = b.split(" ")
    b[0] = float(b[0])
    b[1] = float(b[1])

    distancia = (((b[0] - a[0])**2)+((b[1]-a[1])**2))**(1/2)
    print(f"{distancia:.4f}")

ex_1017()