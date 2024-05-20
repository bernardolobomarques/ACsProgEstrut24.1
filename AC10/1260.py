import sys
from collections import defaultdict

def main():
    entrada = sys.stdin.read
    linhas = entrada().strip().split("\n")
    
    posicao = 0
    casos = int(linhas[posicao])
    posicao += 1
    
    for caso in range(casos):
        if caso > 0:
            print()
        
        contagem_arvores = defaultdict(int)
        total_arvores = 0
        
        while posicao < len(linhas) and linhas[posicao].strip() == '':
            posicao += 1
        
        while posicao < len(linhas) and linhas[posicao].strip() != '':
            arvore = linhas[posicao].strip()
            contagem_arvores[arvore] += 1
            total_arvores += 1
            posicao += 1
        
        for nome_arvore in sorted(contagem_arvores):
            porcentagem = (contagem_arvores[nome_arvore] / total_arvores) * 100
            print(f"{nome_arvore} {porcentagem:.4f}")

if __name__ == "__main__":
    main()
