class Arma: 
    def __init__(self, weapon_name, min_dmg, max_dmg, weapon_id):
        self.weapon_name = weapon_name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.weapon_id = weapon_id

def criar_arma(weapon_name: str, min_dmg: int, max_dmg: int, weapon_id: int):
    if min_dmg <= 0:
        raise ValueError("Uma arma está com dano 0 ou menos! isso é de propósito?")

    arma_criada = Arma(weapon_name, min_dmg, max_dmg, weapon_id)
    return arma_criada

criar_arma(weapon_name="Punhos", min_dmg=1, max_dmg=1,weapon_id=0)         # 0
criar_arma(weapon_name="Adaga Rondel", min_dmg=2, max_dmg=4, weapon_id=1)   # 1

# __name__ guarda literalmente o nome do arquivo (neste caso, "armas").
# Mas, quando você executa o arquivo Python diretamente, ele recebe o __name__ de "__main__"
# Com o if abaixo, caso o arquivo seja importado por outro arquivo (entidades por exemplo), o código dentro do if não é executado.
# Isso protege o código e evita prints, debugs, ou outras linhas de código que é mais relevante para testes sejam executados pelo import.
if __name__ == "__main__":
    pass