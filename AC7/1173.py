posicao0 = int(input())

vetor = [0]*10
vetor[0] = posicao0

for i in range(1,10):
    vetor[i] = vetor[i-1]*2

for _ in range(10):
    print(f"N[{i}] = {vetor[i]}")