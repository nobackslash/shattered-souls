from shatteredsouls.systems.cutscene.intro import introduction_main
from shatteredsouls.systems.util import config

import os #temporario

if __name__ == "__main__":
    os.system("cls")
    try:
        introduction_main() # Play Intro
    except KeyboardInterrupt:
        print("See You Later Alligator!")