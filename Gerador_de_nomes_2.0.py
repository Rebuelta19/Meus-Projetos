from random import choice
from time import sleep
print(25 * '\033[1;33m=-=\033[m')
print('\033[1;36m                ----- GERADOR DE NOMES 2.0 -----\033[m')
n = 'S'
lv = ['a', 'e', 'u', 'i', 'o', 'a', 'ha', 'he']
lc = ['r', 't', 'p', 's', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'c', 'v', 'b', 'n', 'm']
lcm = ['r', 't', 's', 'l', 'v', 'b', 'n', 'm', 'c', 'dr']
lvn = ['a', 'e', 'u', 'i', 'o', 'a', '', 'ar', 'er', 'ir']
pl = str(input('Deseja escolher a primeira letra? (S/N): ')).upper().strip()[0]
if pl == 'S':
    pl1 = str(input('Digite a primeira letra: ')).strip().upper()
    while n == 'S':
        print(25 * '\033[1;33m=-=\033[m')
        print('5 possíveis nomes que começam com a letra \033[1;35m{}\033[m.'.format(pl1))
        for c in range(0, 5):
            l2 = choice(lv)
            l3 = choice(lcm)
            l4 = choice(lv)
            l5 = choice(lcm)
            l6 = choice(lvn)
            lf0 = [pl1, l2, l3, l4, l5, l6]
            lf1 = ''.join(lf0).capitalize()
            print(lf1)
            sleep(0.2)
        print(25 * '\033[1;33m=-=\033[m')
        n = str(input('Deseja gerar mais 5 nomes que começam com a letra \033[1;35m{}\033[m? (S/N): '.format(pl1))).upper().strip()[0]
    print(25 * '\033[1;33m=-=\033[m')
    print('Fim')

if pl == 'N':
     while n == 'S':
        print(25 * '\033[1;33m=-=\033[m')
        print('5 possíveis nomes:')
        for c in range(0, 5):
            l1 = choice(lc)
            l2 = choice(lv)
            l3 = choice(lcm)
            l4 = choice(lv)
            l5 = choice(lcm)
            l6 = choice(lvn)
            lf0 = [l1, l2, l3, l4, l5, l6]
            lf1 = ''.join(lf0).capitalize()
            print(lf1)
            sleep(0.2)
        print(25 * '\033[1;33m=-=\033[m')
        n = str(input('Deseja gerar mais 5 nomes? (S/N): ')).upper().strip()[0]
     print(25 * '\033[1;33m=-=\033[m')
     print('Fim')

