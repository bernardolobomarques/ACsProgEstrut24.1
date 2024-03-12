import random

def main():
    adventure_life = 100
    adventure_att = random.randint(10,20)
    adventure_def = random.randint(1,5)

    monster_life = random.randint(60,80)
    monster_att = random.randint(20,30)

    i = 1

    print(f"Aventureiro: vida ( {adventure_life}, ataque ( {adventure_att} ), defesa ( {adventure_def} ).")
    print(f"Monstro: vida ( {monster_life}, ataque ( {monster_att} ).")

    while adventure_life > 0 or monster_life > 0:
        print(f"Rodada {i}")
        monster_life = monster_life - random.randint(1, adventure_att)
        if monster_life <=0:
            print("O monstro morreu.")
            break
        temp = random.randint(1,monster_att) - adventure_def
        if temp > 0:
            adventure_life = adventure_life - temp
        if adventure_life <= 0:
            print("O aventureiro morreu.")
            break
        print(f"Aventureiro: vida ( {adventure_life}, ataque ( {adventure_att} ), defesa ( {adventure_def} ).")
        print(f"Monstro: vida ( {monster_life}, ataque ( {monster_att} ).")
        i = i+1


main()