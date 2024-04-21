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
    
def ex_1015():
    lista_input = input()
    lista_input = lista_input.split(" ")
    valor_a = int(lista_input[0])
    valor_b = int(lista_input[1])
    valor_c = int(lista_input[2])

    maior_a_b = (valor_a + valor_b + abs(valor_a-valor_b))/2
    if maior_a_b < valor_c:
        print(f"{valor_c} eh o maior")
    else:
        print(f"{int(maior_a_b)} eh o maior")

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

# ex_1017()