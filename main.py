from shatteredsouls.systems.menu.menu import menu, cena
import os

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    repetir = True
    # caso repetir for true, a função vai se repetir, caso for false, vai passar para a próx etapa.
    while repetir:
        repetir = menu()

    escolher_classe = cena()
    print(f'{escolher_classe.name}, você escolheu a classe {escolher_classe.classe}!')
    print(f"Seus atributos são: Strength: {escolher_classe.strength}, Dexterity: {escolher_classe.dexterity}, Vigor: {escolher_classe.vigor}, Intelligence: {escolher_classe.will}, Wisdom: {escolher_classe.wisdom} e Health: {escolher_classe.health}.")
