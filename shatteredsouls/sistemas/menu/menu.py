from entidades import Entity
from char_creation import cena
import msvcrt
import os

print('Bem vindo ao jogo!')


def seta():
    index = 0

    while True:
        os.system('cls')

        if index == 0:
            opt1, opt2, opt3, opt4 = '>>', '  ', '  ', '  '
        elif index == 1:
            opt1, opt2, opt3, opt4 = '  ', '>>', '  ', '  '
        elif index == 2:
            opt1, opt2, opt3, opt4 = '  ', '  ', '>>', '  '
        elif index == 3:
            opt1, opt2, opt3, opt4 = '  ', '  ', '  ', '>>'
        else:
            index = 0
            opt1, opt2, opt3, opt4 = '>>', '  ', '  ', '  '

        print('Navegue com as setas e confirme com Enter ("q" para sair)')
        print(f"{opt1} Start    {opt2} Load    {opt3} Options    {opt4} Exit")

        key = msvcrt.getch()

        if key == b'q':
            return None

        if key == b'\xe0':
            key = msvcrt.getch()
            if key == b'K':
                index = (index - 1) % 4
            elif key == b'M':
                index = (index + 1) % 4
            continue

        if key == b'\r':
            return index


def menu():
    print('=' * 25)
    escolha = seta()

    if escolha is None:
        print('Saindo do menu...')
        return False

    match escolha:
        case 0:
            print('=' * 25)
            print('Você entrou no jogo! :)')
            return False
        case 1:
            print('=' * 25)
            print('Carregando jogo salvo...')
            return True
        case 2:
            print('=' * 25)
            print('Opções: (ainda não implementado)')
            return True
        case 3:
            print('=' * 25)
            print('Você saiu do jogo. :(')
            return False


repetir = True
# caso repetir for true, a função vai se repetir, caso for false, vai passar para a próx etapa.

while repetir:
    repetir = menu()

escolher_classe = cena()
print(f'{escolher_classe.name}, você escolheu a classe {escolher_classe.classe}!')
print(f"Seus atributos são: Strength: {escolher_classe.strength}, Dexterity: {escolher_classe.dexterity}, Vigor: {escolher_classe.vigor}, Intelligence: {escolher_classe.intelligence}, Wisdom: {escolher_classe.wisdom} e Health: {escolher_classe.health}.")


