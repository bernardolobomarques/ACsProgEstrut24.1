def min_movimentos_dama(x1, y1, x2, y2):
    # Se a dama já está na casa de destino, retorna 0
    if x1 == x2 and y1 == y2:
        return 0
    
    # Se a dama está na mesma linha, mesma coluna ou mesma diagonal, retorna 1
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return 1
    
    # Se não, retorna 2, pois em dois movimentos a dama pode chegar à casa de destino
    return 2

# Loop para processar os casos de teste
while True:
    x1, y1, x2, y2 = map(int, input().split())
    
    # Verifica se chegou ao final da entrada
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
    
    # Calcula e imprime o mínimo de movimentos necessários
    print(min_movimentos_dama(x1, y1, x2, y2))
