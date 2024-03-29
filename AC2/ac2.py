"""

PROGRAMAÇÃO ESTRUTURADA 2024.1
AC 2
BERNARDO LOBO MARQUES - MATRICULA: 202401709433
03.03.24

"""


def eq_seg_grau(a, b, c):
    resultado1 = (-b + ((b**2 - 4*a*c)**(1/2)))/(2*a)
    resultado2 = (-b - ((b**2 - 4*a*c)**(1/2)))/(2*a)
    return resultado1, resultado2

def bissexto(ano):
    return((ano%4) == 0 and ((ano % 400 == 0) or not(ano%100 == 0)))

def calcula_salario(valor_hora, num_horas, irpf = 0.275):
    salario_bruto = valor_hora*num_horas
    salario_liquido = salario_bruto - (salario_bruto*irpf)
    return salario_liquido

print(eq_seg_grau(1,1,1))
print(bissexto(1900))
print(calcula_salario(10, 10))
