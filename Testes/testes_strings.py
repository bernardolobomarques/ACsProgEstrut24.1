# Contar ocorrências de uma substring em uma string
print("olá, mundo!".count("o"))

# Localizar uma substring em uma string
# Indica o índice do primeiro caractere da substring
print("olá, mundo!".find("olá,"))
print("olá, mundo!".find("Olá,")) # Substring não é encontrada, retorna -1

# A função index também obtém o índice do primeiro caractere da substring
# No entanto, a função retorna uma exceção caso não localize a substring
# Não recomendo utilizar essa função!
print("olá, mundo!".index("olá,"))
# print("olá, mundo!".index("Olá,")) -> vai subir uma exceção do tipo ValueError

# Divide uma string, considerando um separador
# Retorna uma lista com as substrings obtidas
print("olá, mundo!".split(","))

# Une os elementos de uma lista de strings, adotando o separador definido
print(" - ".join(["1", "2", "3", "4", "5"]))

# Coloca todos os caracteres com letras maiúsculas ou minúsculas
# Gosto de usar essas funções para comparar strings e inputs de usuários
print("Olá, mundo".upper())
print("Olá, mundo".lower())

# Coloca o primeiro caractere em caixa alta
print("o rato roeu a roupa do rei de roma".capitalize())

# Coloca o primeiro caractere de cada palavra em caixa alta
print("o rato roeu a roupa do rei de roma".title())

# Troca o case (maiúscula por minúscula)
print("Olá!".swapcase())

# Identifica se a string é de algum dos tipos listados
print("oi".isupper())         # é maiúscula
print("oi".islower())         # é minúscula
print("Olá Mundo".istitle())  # tem o estilo de título
print("oi1".isalnum())        # possui apenas caracteres alfanuméricos
print("oi1".isalpha())        # possui apenas letras
print("oi1".isdigit())        # possui apenas números, 0-9
print("oi1".isnumeric())      # possui apenas números, em qualquer notação
                              # por exemplo, 三 é o ideograma chinês para 3
                              # a função isnumeric() retorna True
                              # a função isdigit() retorna False
print("   ".isspace())        # indica se possui apenas espaços

# Funções para organização de strings
print("Olá, mundo".ljust(40)) # alinha o texto à esquerda e preenche com espaços
                              # os demais caracteres
print("Olá, mundo".rjust(40)) # alinha o texto à direita e preenche com espaços
                              # os demais caracteres
print("Olá, mundo".center(40))# centraliza o texto e preenche com espaços os
                              # demais caracteres
print("  123  ".lstrip())     # remove espaços em branco à esquerda
print("  123  ".rstrip())     # remove espaços em branco à direita
print("  123  ".strip())     # remove espaços em branco à esquerda e à direita

# Identifica se a string começa ou termina com uma determinada substring
print("Olá, mundo!".startswith("Olá"))
print("Olá, mundo!".endswith("Olá"))

# Substitui uma substring dentro de uma string por outra substring
print("Olá, mundo!".replace("Olá, ", "olá, "))

print("-" * 30)

nome = "Victor"
preco_total = 29.99
quantidade = 16

print("Dados da venda")  # veja que não há inclusão de variáveis, logo não
                         # usamos uma f-string
print(f"Nome: {nome}")

# A formatação abaixo indica que o número é inteiro e deve possuir 4
# caracteres. O que não for preenchido pelos números será preenchido por espaços
print(f"Quantidade comprada: {quantidade:4d}")
print(f"Preço total: {preco_total}")

# A formatação abaixo indica que o número possui até 4 caracteres, com
# 2 caracteres à direita do ponto, e é do tipo float
print(f"Valor unitário: {(preco_total / quantidade):4.2f}")