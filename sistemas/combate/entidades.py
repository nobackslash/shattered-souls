from math import ceil

class Entity:
    def __init__(self, name, strength, dexterity, vigor, intelligence, wisdom):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.vigor = vigor
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.rightHand = "Unarmed"
        self.leftHand = "Unarmed"
        self.health = ceil(8 + (self.vigor * 0.75) + (self.strength * 0.25))

    def debugPrint(self):
        print(f"Entity: {self.name}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Vigor: {self.vigor}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Right Hand: {self.rightHand}")
        print(f"Left Hand: {self.leftHand}")
        print(f"Health: {self.health}")

if __name__ == "__main__":
    Entity("Goblin", 5, 3, 4, 2, 1).debugPrint()