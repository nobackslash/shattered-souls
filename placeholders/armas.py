armas = []
class Arma: 
    def __init__(self, nome, dano):
        self.id = len(armas) # Notei que self.id não se tem muita utilidade, só mais para debug mesmo.
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

criar_arma("Punhos", 1)         # 0
criar_arma("Adaga Rondel", 2)   # 1

# __name__ guarda literalmente o nome do arquivo (neste caso, "armas").
# Mas, quando você executa o arquivo Python diretamente, ele recebe o __name__ de "__main__"
# Com o if abaixo, caso o arquivo seja importado por outro arquivo (entidades por exemplo), o código dentro do if não é executado.
# Isso protege o código e evita prints, debugs, ou outras linhas de código que é mais relevante para testes sejam executados pelo import.
if __name__ == "__main__":
    if isinstance(armas[0], Arma): #isinstance é uma forma mais elegante comparado com ```if type(armas[0]) == Arma```
    # Uma dica, usar isinstance também ativa o sense do código, se eu não colocar o isintance, debug_info ficaria em branco.
    # mas com o isinstance, ele mostra as funções, variáveis, e outros atributos connectados com a classe.
        print(armas[0].debug_info())
        print(armas[0].obter_dano())