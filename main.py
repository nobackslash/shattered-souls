from shatteredsouls.systems.menu.menu import menu, cena
from shatteredsouls.systems.combat.entities import Entity
import os

def main1():
    os.system('cls' if os.name == 'nt' else 'clear')
    repetir = True
    # caso repetir for true, a função vai se repetir, caso for false, vai passar para a próx etapa.
    while repetir:
        repetir = menu()

    escolher_classe = cena()
    if isinstance(escolher_classe, Entity): # É igual fazer escolher_classe == Entity, mas é mais seguro, pois verifica se o objeto é do tipo Entity, e não apenas se é igual a Entity.
        print(f'{escolher_classe.name}, você escolheu a classe {escolher_classe.classe}!')
        print(f"Seus atributos são: Força: {escolher_classe.strength}, Destreza: {escolher_classe.dexterity}, Vigor: {escolher_classe.vigor}, Vontade: {escolher_classe.will}, Sabedoria: {escolher_classe.wisdom} e Vida: {escolher_classe.health}.")

def main2():
    from shatteredsouls.systems.cutscene.intro import main
    main()

main2()