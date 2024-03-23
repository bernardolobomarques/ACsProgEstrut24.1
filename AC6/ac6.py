def ex_1000():
    print("Hello World!")

def ex_1001():
    a = int(input())
    b = int(input())
    x = a + b
    print("X =", x)

def ex_1010():
    a = int(input())
    b = int(input())
    c = float(input())

    d = int(input())
    e = int(input())
    f = float(input())

    valor = e*f + b*c
    print(f"VALOR A PAGAR: R$ {valor:.2f}")

# ex_1010()
    
def ex_1013():
    x = int(input())
    y = int(input())
    z = int(input())

    if x>y and x > z:
        print(x, "eh o maior")
    elif y>z and y>x:
        print(y, "eh o maior")
    elif z>y and z>x:
        print(z, "eh o maior")

ex_1013()