armas = []
class Arma: 
    def __init__(self, nome, dano):
        self.id = len(armas)
        self.nome = nome
        self.dano = dano

    def obter_dano(self):
        return self.dano

    def debug_info(self):
        print(f"Identificador: {self.id}, Nome: {self.nome}, Dano: {self.dano}")

def criar_arma(arg_nome: str, arg_dano: int, lista_armas: list=armas):
    if arg_dano <= 0:
        raise "Uma arma está com dano 0 ou menos! isso é de propósito?"

    arma_criada = Arma(arg_nome, arg_dano)
    lista_armas.append(arma_criada)
    return arma_criada

criar_arma("Punhos", 1)
criar_arma("Adaga Rondel", 2)

if isinstance(armas[0], Arma):
    print(armas[0].debug_info())
    print(armas[0].obter_dano())