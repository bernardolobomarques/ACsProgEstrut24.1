"""
AC3 PROGRAMAÇÃO ESTRUTURADA 2024.1
BERNARDO LOBO MARQUES - MATRÍCULA 202401709433
05.03.24

"""

def determina_tipo_triangulo(a,b,c):
    #A SOMA DE DOIS LADOS TEM QUE SER MENOR OU IGUAL A DO TERCEIRO
    if ((a + b >= c) and (a + c >= b) and (b + c >= a)):
        if (a == b and b == c):
            return ("O triangulo é equilatero")
        elif ((a == b) or (b == c) or (a == c)):
            return ("O triangulo é isoceles")
        elif ((a != b) and (b !=c) and (a != c)):
            return ("O triangulo é escaleno")
    return ("Não é um triangulo")

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

testa_triangulo()
print("\n")

def dia_semana(dia):
    if dia == 1:
        return "Domingo"
    elif dia == 2:
        return "Segunda-Feira"
    elif dia == 3:
        return "Terça-Feira"
    elif dia == 4:
        return "Quarta-Feira"
    elif dia == 5:
        return "Quinta-Feira"
    elif dia == 6:
        return "Sexta-Feira"
    elif dia == 7:
        return "Sabado"
    return ""

def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

testa_dia_semana()
print("\n")

def soma(x,y):
    return x+y

def subtracao(x,y):
    return x-y

def multiplicacao(x,y):
    return x*y

def divisao(x,y):
    return x/y

def calculadora():
    x = float(input("Qual o primeiro numero? "))
    y = float(input("Qual o segundo numero? "))
    controle = input("Qual operacao gostaria de fazer? ")

    match (controle):
        case "soma":
            print("O resultado da operacao e", soma(x,y))
        case "subtração":
            print("O resultado da operacao e", subtracao(x,y))
        case "multiplicação":
            print("O resultado da operacao e", multiplicacao(x,y))
        case "divisão":
            print("O resultado da operacao e", divisao(x,y))
        case _:
            print("Operacao invalida")

calculadora()