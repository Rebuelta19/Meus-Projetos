print(20 * '\033[1;33m=-=\033[m')
print('\033[1;36mBora jogar jokenpô!\nJokeeeen...\033[m')
v1 = str(input('Pedra, papel ou tesoura?\n')).strip().lower()
print('\033[1;36mPÔ!\033[m')
from time import sleep
from random import choice
from emoji import emojize
l1 = ['Pedra', 'Papel', 'Tesoura']
r1 = choice(l1)
if 'Pedra' in r1 and 'papel' in v1:
    print(emojize('Você mostra sua mão: :raised_hand:'))
    sleep(1)
    print(emojize('Logo em seguida a maquiná mostra a dela: :oncoming_fist:'))
    sleep(2)
    print('\033[1;36mPapel embrulha pedra, droga perdi...\033[m')
    print(20 * '\033[1;33m=-=\033[m')
    print('Parabéns você venceu!')
elif 'Pedra' in r1 and 'tesoura' in v1:
    print(emojize('Você mostra sua mão: :victory_hand:'))
    sleep(1)
    print(emojize('Logo em seguida a maquiná mostra a dela: :oncoming_fist:'))
    sleep(2)
    print('\033[1;36mYES, pedra estrasalha a tesoura, toma essa!\033[m')
    print(20 * '\033[1;33m=-=\033[m')
    print('Você perdeu.')
elif 'Pedra' in r1 and 'pedra' in v1:
    print(emojize('Você mostra sua mão: :oncoming_fist:'))
    sleep(1)
    print(emojize('Logo em seguida a maquiná mostra a dela: :oncoming_fist:'))
    sleep(2)
    print('\033[1;36mDroga, empate? vamos tentar outra vez.')
    print(20 * '\033[1;33m=-=\033[m')
    print('Empate, tente outra vez.')
elif 'Papel' in r1 and 'papel' in v1:
    print(emojize('Você mostra sua mão: :raised_hand:'))
    sleep(1)
    print(emojize('Logo em seguida a maquiná mostra a dela: :raised_hand:'))
    sleep(2)
    print('\033[1;36mDroga, empate? vamos tentar outra vez.')
    print(20 * '\033[1;33m=-=\033[m')
    print('Empate, tente outra vez.')
elif 'Papel' in r1 and 'tesoura' in v1:
    print(emojize('Você mostra sua mão: :victory_hand:'))
    sleep(1)
    print(emojize('Logo em seguida a maquiná mostra a dela: :raised_hand:'))
    sleep(2)
    print('\033[1;36mTesoura corta o papel, droga perdi...\033[m')
    print(20 * '\033[1;33m=-=\033[m')
    print('Parabéns você venceu!')
elif 'Papel' in r1 and 'pedra' in v1:
    print(emojize('Você mostra sua mão: :oncoming_fist:'))
    sleep(1)
    print(emojize('Logo em seguida a maquiná mostra a dela: :raised_hand:'))
    sleep(2)
    print('\033[1;36mYES, papel embrulha pedra, toma essa!\033[m')
    print(20 * '\033[1;33m=-=\033[m')
    print('Você perdeu.')
elif 'Tesoura' in r1 and 'papel' in v1:
    print(emojize('Você mostra sua mão: :raised_hand:'))
    sleep(1)
    print(emojize('Logo em seguida a maquiná mostra a dela: :victory_hand:'))
    sleep(2)
    print('\033[1;36mYES, tesoura corta papel, toma essa!\033[m')
    print(20 * '\033[1;33m=-=\033[m')
    print('Você perdeu.')
elif 'Tesoura' in r1 and 'tesoura' in v1:
    print(emojize('Você mostra sua mão: :victory_hand:'))
    sleep(1)
    print(emojize('Logo em seguida a maquiná mostra a dela: :victory_hand:'))
    sleep(2)
    print('\033[1;36mDroga, empate? vamos tentar outra vez.')
    print(20 * '\033[1;33m=-=\033[m')
    print('Empate, tente outra vez.')
elif 'Tesoura' in r1 and 'pedra' in v1:
    print(emojize('Você mostra sua mão: :oncoming_fist:'))
    sleep(1)
    print(emojize('Logo em seguida a maquiná mostra a dela: :victory_hand:'))
    sleep(2)
    print('\033[1;36mPedra estrasalha a tesoura, droga perdi...\033[m')
    print(20 * '\033[1;33m=-=\033[m')
    print('Parabéns você venceu!')
else:
    print('\033[1;36mEstamos jogando jokenpô aqui, {}? Vamos lá digite algo válido... '.format(v1))