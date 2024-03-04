"""

PROGRAMAÇÃO ESTRUTURADA 2024.1
AC 2
BERNARDO LOBO MARQUES - MATRICULA: 202401709433
03.03.24

"""


def exercicio1_1(a,b,c):
    resultado1 = (-b + ((b**2 - 4*a*c)**(1/2)))/(2*a)
    resultado2 = (-b - ((b**2 - 4*a*c)**(1/2)))/(2*a)
    print("A primeira raiz da equacao e", resultado1, "\n", "E a segunda raiz da equacao e", resultado2)
    return(resultado1, resultado2)

def exercicio1_2(ano):
    print((ano%4) == 0 and ((ano % 400 == 0) or not(ano%100 == 0)))

def calcula_salario(valor_hora, num_horas, irpf = 0.275):
    salario_bruto = valor_hora*num_horas
    salario_liquido = salario_bruto - (salario_bruto*irpf)
    return salario_liquido