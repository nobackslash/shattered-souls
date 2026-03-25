from math import ceil as mathCeil
from random import randint as randomInterger

class Entidade:
    def __init__(self, nome, forca, destreza, vigor, vontade, conhecimento):
        # PRECISAMOS DE MAIS OU MENOS ATRIBUTOS?
        self.nome         = nome
        self.forca        = forca
        self.destreza     = destreza
        self.vigor        = vigor
        self.vontade      = vontade
        self.conhecimento = conhecimento
        self.maoDireita   = 0
        self.maoEsquerda  = 0
        self.vida         = mathCeil(8 + (self.vigor * 0.75) + (self.strength * 0.25))
        self.vidaMaxima   = self.vida

    def debugPrint(self):
        # DEBUG SÓ PARA CONFIRMAR OS DADOS DA ENTIDADE, UTILIZÁVEL EM QUALQUER AREA.
        print(f"Nome:                   {self.nome}")
        print(f"Forca:                  {self.forca}")
        print(f"Destreza:               {self.destreza}")
        print(f"Vigor:                  {self.vigor}")
        print(f"Vontade:                {self.vontade}")
        print(f"Conhecimento:           {self.conhecimento}")
        print(f"Mão Direita  (ID):      {self.maoDireita}")
        print(f"Mão Esquerda (ID):      {self.maoEsquerda}")
        print(f"Vida:                   {self.vida}")

    def attack(self, alvo: Entidade):
        # PRECISAMOS DEFINIR COMO QUE ATAQUES SÃO FEITOS, SE VAI USAR SKILL DA ENTIDADE, UM 1d20, OU OUTRAS FORMAS.
        print(f"{self.nome} está atacando {alvo.nome} com {self.maoDireita} e {self.maoEsquerda}!")
        if randomInterger(1, 20) + self.forca > 10:  # Simples teste de ataque
            damage = mathCeil(self.forca * 0.5)
            alvo.vida -= damage
            print(f"Acertou! {alvo.nome} recebeu {damage} de dano. Saúde restante: {alvo.vida}")

if __name__ == "__main__":
    Goblin    = Entidade("Goblin", 5, 3, 4, 2, 1).debugPrint()
    Heroi     = Entidade("Herói", 4, 5, 4, 1, 1).debugPrint()
    Goblin.attack(Heroi)