salario_base =float(input())

if salario_base<= 400:
    reajuste = 15
elif salario_base > 400 and salario_base <= 800:
    reajuste = 12
elif salario_base > 800 and salario_base <= 1200:
    reajuste = 10
elif salario_base > 1200 and salario_base <= 2000:
    reajuste = 7
elif salario_base > 2000:
    reajuste = 4

salario_novo = salario_base * (reajuste*0.01) + salario_base

print(f"Novo salario: {salario_novo:.2f}")
print(f"Reajuste ganho: {salario_base * (reajuste*0.01):.2f}")
print(f"Em percentual: {reajuste} %")