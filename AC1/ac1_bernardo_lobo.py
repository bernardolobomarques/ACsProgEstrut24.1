"""

PROGRAMAÇÃO ESTRUTURADA 2024.1
AC 1
BERNARDO LOBO MARQUES - MATRICULA: 202401709433
27.02.24

"""


def exercicio1():
    a = int(input("Qual o valor do \"a\" da funcao? "))
    b = int(input("Qual o valor do \"b\" da funcao? "))
    c = int(input("Qual o valor do \"c\" da funcao? "))

    resultado1 = (-b + ((b**2 - 4*a*c)**(1/2)))/2
    resultado2 = (-b - ((b**2 - 4*a*c)**(1/2)))/2
    print(resultado1, "\n", resultado2)
    return(resultado1, resultado2)

def exercicio2():
    ano = int(input("Qual o ano que gostaria de saber se e ou nao bissexto? "))
    controle = ano%4
    print(controle == 0)


def main():
    #  exercicio1()
    #  exercicio2()

#Deixei comentado para caso queira testa-los um por um, portanto o erro na main()
main()