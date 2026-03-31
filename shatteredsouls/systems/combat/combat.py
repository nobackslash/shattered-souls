import os
import random
from weapon_list import weapon_list
from entities import Entity
from playerCombatChoices import drawPlayerOptions, processPlayerChoice

def get_weapon(weapon_id: int):
    return weapon_list[weapon_id]["name"]

def calc_dmg(weapon_id: int, entity: Entity):
    min = weapon_list[weapon_id]["min_dmg"]
    max = weapon_list[weapon_id]["max_dmg"]
    random_dmg = random.randint(min, max)
    if (entity.strength + random_dmg) == (entity.strength + max):
        print(f"\033[1;31mCritical hit!\033[0m")
        return 0
    return entity.strength + random_dmg

def melee_atack(attacker: Entity, defender: Entity):
    damage = calc_dmg(weapon_id=attacker.rightHand, entity=attacker)
    defender.health -= damage
    print(f"{attacker.name} atacou {defender.name} com {get_weapon(attacker.rightHand)}!")
    print(f"{defender.name} recebeu {damage} de dano! Saúde restante: {defender.health}")

def drawEntitiesStatsUI(entity1: Entity, entity2: Entity):
    # we have 120 columns
    string = ""
    # print("|"+f"{entity1.name} (Health: {entity1.health})".center(58) + "|" + f"{entity2.name} (Health: {entity2.health})".center(58)+"|")
    # print("|"+f"(Mão Direita: {get_weapon(entity1.rightHand)})".center(58) + "|" + f"(Mão Direita: {get_weapon(entity2.rightHand)})".center(58)+"|")
    string += ("|"+f"{entity1.name} (Health: {entity1.health})".center(58) + "|" + f"{entity2.name} (Health: {entity2.health})".center(58)+"|")
    string += ("\n|"+f"(Mão Direita: {get_weapon(entity1.rightHand)})".center(58) + "|" + f"(Mão Direita: {get_weapon(entity2.rightHand)})".center(58)+"|")
    return string

def drawCombatLog(log):
    pass

def engage_combat(entity1: Entity, entity2: Entity):
    print("Entering combat...")
    while entity1.health > 0 and entity2.health > 0:
        entstr = drawEntitiesStatsUI(entity1, entity2)
        optstr = drawPlayerOptions()
        print(entstr)
        print(optstr)
        processPlayerChoice()

    
    print("Combat ended!")
    print(f"{entity1.name} health: {entity1.health}")

if __name__ == "__main__":
    os.system('cls')
    Goblin = Entity("Goblin", "BOT", 5, 3, 40, 2, 1)
    Heroi = Entity("Herói", "BOT", 4, 5, 40, 1, 1)
    engage_combat(Heroi, Goblin)