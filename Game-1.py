from random import randint
from time import sleep
print(25 * '\033[1;33m=-=\033[m')
print('\033[1;36mEu dúvido você acertar o número em que eu estou pensando entre 1 e 10')
print('Deixe me ver', end='')
sleep(0.2)
print('.', end= '')
sleep(0.5)
print('.', end= '')
sleep(0.5)
print('.', end= '')
sleep(0.5)
print(' Ok, tente advinhar.')
t = 1
r = 0
s = ''
r = randint(1, 10)
while r != s:
    s = str(input('\033[mSeu palpite é: '))
    s1 = s.isnumeric()
    if s1 == True:
        s = int(s)
        if s <= 10:
            if r != s:
                t += 1
                if s < r:
                    print('\033[1;36mÉ um valor maior.')
                else:
                    print('\033[1;36mÉ um valor menor.')
        else:
            print('\033[1;31m{} não é um número válido, \033[1;36mdigite um número de entre 1 e 10.\033[m'.format(s))
            print(25 * '\033[1;33m=-=\033[m')
    else:
        print('\033[1;31m{} não é um número, \033[1;36mdigite um número entre 1 e 10.\033[m'.format(s))
        print(25 * '\033[1;33m=-=\033[m')
print('\033[1;36mDroga, você acertou hahaha.')
print(25 * '\033[1;33m=-=\033[m')
if t <= 2:
    print('Tentativas: {}\n\033[1;34mParabéns você foi muito bem!\033[m'.format(t))
elif t > 2 and t <= 3:
    print('Tentativas: {}\n\033[1;36mVocê foi bem!\033[m'.format(t))
elif t > 3 and t <= 5:
    print('Tentativas: {}\n\033[1;36mVocê não foi muito bem.\033[m'.format(t))
elif t > 5:
    print('Tentaivas: {}\n\033[1;31mVocê foi péssimo!\033[m'.format(t))
print(25 * '\033[1;33m=-=\033[m')
print('Fim.')