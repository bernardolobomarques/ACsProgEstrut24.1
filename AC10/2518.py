import math
while True:
    try:
        degraus = int(input())
        h, c, l = input().split()

        hipotenusa = math.sqrt((int(c) ** 2) + (int(h) ** 2))
        hipotenusa *= (int(l)/100*int(degraus))/100
        print('%.4f'%hipotenusa)

    #Até eu descobrir como fazia isso aq...
    except EOFError:
        break