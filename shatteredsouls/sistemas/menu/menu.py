from entidades import Entity
from char_creation import cena


print('Bem vindo ao jogo!')

def menu():

    try:
        print('=' * 25)
        escolha = int(input('Escolha uma opção '))
        
        match escolha:
            case 1:
                print('=' * 25)
                print('Você entrou no jogo! :)') 
                return False
            case 2:
                print('=' * 25)
                print('Você saiu do jogo. :(')

                return False
            case 3:
                print('=' * 25)
                print('Carregando...')
                return False
            case 4:
                print('=' * 25)
                print('Opções:')
                return False

    except:
        print('=' * 25)
        print('Ocorreu um erro.')
        print('=' * 25)
        return True
repetir = True
#caso repetir for true, a função vai se repetir, caso for false, vai passar para a próx etapa.

while repetir:
    repetir = menu()

escolher_classe = cena()
print(f'{escolher_classe.name}, você escolheu a classe {escolher_classe.classe}!')
print(f"Seus atributos são: Strength: {escolher_classe.strength}, Dexterity: {escolher_classe.dexterity}, Vigor: {escolher_classe.vigor}, Intelligence: {escolher_classe.intelligence}, Wisdom: {escolher_classe.wisdom} e Health: {escolher_classe.health}.")


