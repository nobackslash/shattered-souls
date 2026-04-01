import time
import os

from shatteredsouls.systems.menu import intro

def exit_intro():
    os.system('cls')
    print("\n" * (intro.HEIGHT // 2 - 1))
    intro.type_line("You died.")
    time.sleep(1.5)
    intro.wipe_line()
    intro.type_line("But this is not the end...")
    time.sleep(1.5)
    intro.wipe_line()
    intro.type_line("Your soul lingers, trapped in this realm of shadows.")
    time.sleep(1.5)
    intro.wipe_line()
    intro.type_line("Will you find a way to escape, or will you be lost forever?")
    time.sleep(2.5)