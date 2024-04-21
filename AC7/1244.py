n_testes = int(input())
for i in range(n_testes):
    string_lida = input()
    lista_string_lida = string_lida.split(" ")
    lista_ordenada = sorted(lista_string_lida, key=len, reverse=True)
    print(" ".join(lista_ordenada))