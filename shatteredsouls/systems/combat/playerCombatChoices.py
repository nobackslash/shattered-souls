import time
import msvcrt

def Combate_Atacar():
    print("A")
def Combate_UsarItem():
    print("B")
def Combate_Fugir():
    print("C")

opções = {
    "Atacar": Combate_Atacar,
    "Usar Item": Combate_UsarItem,
    "Fugir": Combate_Fugir
}

choiceIndex = 0
escolhas = []
recentKey = ""
chosenOption = ""
arrowKeyFlag = False

def processPlayerChoice():
    global arrowKeyFlag, choiceIndex, recentKey, chosenOption
    recentKey = msvcrt.getch()
    if recentKey == b'\xe0':
        arrowKeyFlag = True
    elif arrowKeyFlag:
        choiceIndex += (1 if recentKey == b'M' else -1 if recentKey == b'K' else 0)
        arrowKeyFlag = False

    if recentKey == b'\r':
        try:
            # print("EXECUTANDO FUNCTION")
            opções[chosenOption]()
        except Exception as err:
            print("ERRO: ", err)

def drawPlayerOptions():
    global recentKey, choiceIndex, arrowKeyFlag, chosenOption
    optionsLine = ""
    index = 1
    # print(choiceIndex)
    if recentKey == b'\xe0':
        return

    for name in opções.keys():
        if choiceIndex == index - 1:
            optionsLine += ">> "
            chosenOption = name
            
        optionsLine += f"{index} - {name} "
        index += 1
    
    # optionsLine += "\n"
    return optionsLine

if __name__ == "__main__":
    while True:
       string = drawPlayerOptions()
       if string:
        print(string)
       processPlayerChoice()