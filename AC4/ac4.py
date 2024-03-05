def ler_nome():
    nome = input("Qual seu nome? ")
    return nome

def ler_notas():
    ap1 = float(input("Qual a nota da ap1? "))
    ap2 = float(input("Qual a nota da ap2? "))
    asub = float(input("Qual a nota da as? "))
    ac = float(input("Qual a nota da ac? "))
    return ap1,ap2,asub,ac

def validar_notas(ap1, ap2, asub, ac):
    if ap1<0 or ap1>10:
        return False
    elif ap2<0 or ap2>10:
        return False
    elif asub<0 or asub>10:
        return False
    elif ac<0 or ac>10:
        return False
    return True

def duas_maiores_notas(ap1,ap2,asub):
    if asub > ap1:
        return asub, ap2
    elif asub> ap2:
        return ap1, asub
    return ap1,ap2

def fazer_media(n1, n2, ac):
    media = ((n1+n2)*0.4) + (ac*0.2)
    return media

def informar_aprovacao(media, nome):
    media_arredondada = round(media, 2)
    if media>= 7:
        print("O aluno", nome, "foi aprovado com a media", media_arredondada)
    else:
        print("O aluno", nome, "foi reprovado com a media", media_arredondada)

def main():
    nome = ler_nome()
    if nome:
        ap1,ap2,asub,ac = ler_notas()
        if validar_notas(ap1,ap2,asub,ac):
            n1,n2 = duas_maiores_notas(ap1,ap2,asub)
            media = fazer_media(n1,n2,ac)
            informar_aprovacao(media, nome)

main()