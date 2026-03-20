from math import ceil as mathCeil
from random import randint as randomInterger

class Entity:
    def __init__(self, name, strength, dexterity, vigor, intelligence, wisdom):
        self.name = name
        # PRECISAMOS DE MAIS OU MENOS ATRIBUTOS?
        self.strength = strength
        self.dexterity = dexterity
        self.vigor = vigor
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.rightHand = "Unarmed"
        self.leftHand = "Unarmed"
        self.health = mathCeil(8 + (self.vigor * 0.75) + (self.strength * 0.25))

    def debugPrint(self):
        # DEBUG SÓ PARA CONFIRMAR OS DADOS DA ENTIDADE, UTILIZÁVEL EM QUALQUER AREA.
        print(f"Entity: {self.name}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Vigor: {self.vigor}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Right Hand: {self.rightHand}")
        print(f"Left Hand: {self.leftHand}")
        print(f"Health: {self.health}")

    def attack(self, alvo):
        # PRECISAMOS DEFINIR COMO QUE ATAQUES SÃO FEITOS, SE VAI USAR SKILL DA ENTIDADE, UM 1d20, OU OUTRAS FORMAS.
        print(f"{self.name} está atacando {alvo.name} com {self.rightHand} e {self.leftHand}!")
        if randomInterger(1, 20) + self.strength > 10:  # Simples teste de ataque
            damage = mathCeil(self.strength * 0.5)
            alvo.health -= damage
            print(f"Acertou! {alvo.name} recebeu {damage} de dano. Saúde restante: {alvo.health}")

if __name__ == "__main__":
    Goblin = Entity("Goblin", 5, 3, 4, 2, 1).debugPrint()
    Heroi = Entity("Herói", 4, 5, 4, 1, 1).debugPrint()
    Goblin.attack(Heroi)