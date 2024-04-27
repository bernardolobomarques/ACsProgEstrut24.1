n_testes = int(input())
for _ in range(n_testes):
    qtd_comida = float(input())
    cont = 0
    while qtd_comida > 1:
        qtd_comida = qtd_comida*0.5
        cont += 1
    
    print(f"{cont} dias")