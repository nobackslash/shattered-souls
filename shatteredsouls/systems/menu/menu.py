from shatteredsouls.systems.menu.character_creation import cena
from shatteredsouls.systems.combat.entities import Entity
import msvcrt
import os


def seta():
    index = 0

    while True:
        os.system('cls')

        match index:
            case 0:
                opt1 = "\033[95mStart\033[0m"
                opt2 = "Load"
                opt3 = "Options"
                opt4 = "Exit"
            case 1:
                opt1 = "Start"
                opt2 = "\033[95mLoad\033[0m"
                opt3 = "Options"
                opt4 = "Exit"
            case 2:
                opt1 = "Start"
                opt2 = "Load"
                opt3 = "\033[95mOptions\033[0m"
                opt4 = "Exit"
            case 3:
                opt1 = "Start"
                opt2 = "Load"
                opt3 = "Options"
                opt4 = "\033[95mExit\033[0m"
            case _ if index > 3:
                index = 0
                opt1 = "\033[95mStart\033[0m"
                opt2 = "Load"
                opt3 = "Options"
                opt4 = "Exit"
            case _ if index < 0:
                index = 3
                opt1 = "Start"
                opt2 = "Load"
                opt3 = "Options"
                opt4 = "\033[95mExit\033[0m"

        print('Navegue com as setas e confirme com Enter ("q" para sair)')
        print(f"{opt1}    {opt2}    {opt3}    {opt4}".center(160))

        key = msvcrt.getch()

        if key == b'q':
            return None

        if key == b'\xe0':
            key = msvcrt.getch()
            if key == b'K':
                index -= 1
            elif key == b'M':
                index += 1
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


if __name__ == "__main__":
    print('Bem vindo ao jogo!')




