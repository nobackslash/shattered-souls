from shatteredsouls.systems.combat.entities import Entity
def cena():
    name1 = str(input('Escolha o seu nome: ')).capitalize()
    # jogador = Entity()
    classe = str(input('Escolha a sua classe: Mago, Guerreiro, Paladino, Clerigo ou Valquiria: ')).upper()
    try:
        match classe:
            case "MAGO":
                classe = Entity(name1, classe, 2, 3, 4, 5, 1)
                return classe
            case "GUERREIRO":
                classe = Entity(name1, classe, 5, 3, 4, 2, 1)
                return classe
            case "PALADINO":
                classe = Entity(name1, classe, 3, 5, 4, 1, 2)
                return classe
            case "CLERIGO":
                classe = Entity(name1, classe, 1, 3, 4, 5, 2)
                return classe
            case "VALQUIRIA":
                classe = Entity(name1, classe, 1, 5, 2, 4, 3)
                return classe
    except:

        # repetir = True
    
        while classe not in ["MAGO", "GUERREIRO", "PALADINO", "CLERIGO", "VALQUIRIA"]:
            print('Ocorreu um erro, escolha uma classe válida.')
            classe = cena()
            return classe


