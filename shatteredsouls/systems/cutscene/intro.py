import time
import os
import random
import pygame
import asyncio
import atexit
import shutil
import re

import shatteredsouls.assets as assets
from shatteredsouls.systems.menu import exit
from shatteredsouls.assets.text.title import ascii_title
from shatteredsouls.systems.menu.style_effects import center_ansi, colorize_char
from shatteredsouls.systems.util.lines import color_line
import shatteredsouls.systems.ui.terminal as ui
from shatteredsouls.systems.cutscene.easterEggDialogue import linesEaster

# reuse menu helpers from the original menu module to keep that file authoritative
from shatteredsouls.systems.menu.menu import format_menu_line, interact_menu

# cursor helpers live in the UI module
from shatteredsouls.systems.ui.terminal import hide_cursor, show_cursor
atexit.register(show_cursor)

WIDTH = shutil.get_terminal_size().columns
HEIGHT = shutil.get_terminal_size().lines


glich_fx = "░▒▓█"
ANSI_REGEX = re.compile(r'\x1b\[[0-9;]*m')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_line(text):
    current = ""
    for char in text:
        current += char
        colorArgs = {"died": "red",
                     "you": "purple", 
                     "die": "red", 
                     "end": "purple",
                     "wrong": "red", 
                     "Your": "purple",
                     "your": "purple", 
                     "forever": "red"} # example: color "you" in purple and "die" in red
        display = color_line(current)
        print("\r" + center_ansi(display, WIDTH).ljust(WIDTH), end="", flush=True)
        time.sleep(0.04 if char != " " else 0.08)
    time.sleep(0.9)


def wipe_line():
    print("\r" + " " * WIDTH, end="", flush=True)


def glitch_effect(text: str, intensity: float = 0.1) -> str:
    global glich_fx

    glitched_text = ""
    for char in text:
        if random.random() < intensity: # chance of glitching each character
            glitched_text += random.choice(glich_fx)
        else:
            glitched_text += char

    return glitched_text


def glitch_disappear(text_string):
    for i in range(10):
        intensity = (i + 1) / 10
        glitched = glitch_effect(text_string, intensity=intensity)
        visible_chars = int(len(text_string) * (1 - intensity))
        glitched = glitched[:visible_chars]
        print("\r" + center_ansi(f"\033[2;35mm{glitched}\033[0m", WIDTH).ljust(WIDTH), end="", flush=True)
        time.sleep(0.1)


def final_phase(text):
    try:
        awake = pygame.mixer.Sound(assets.sfx["glitch_sfx"])
        awake.play()

        colorArgs = {"░": "purple", "▒": "purple", "▓": "purple", "█": "purple"}
        glitch_disappear(color_line(text))

        earlyCutoff = 3
        time.sleep(max(0, awake.get_length() - earlyCutoff))
    except Exception:
        time.sleep(1)
    clear()


def show_title():
    try:
        pygame.mixer.music.load(assets.sfx["title_sfx"])
        pygame.mixer.music.play()
    except Exception:
        pass

    original_lines = [list(line) for line in ascii_title.split("\n")]
    lines = [row.copy() for row in original_lines]
    height = len(lines)

    return lines, original_lines, height


async def glitch_title_with_menu(original_lines, menu_state):
    step = 0
    height = len(original_lines)
    menu_start_line = min(HEIGHT - 4, height + 4)
    last_index = None

    # initial static menu render (before animation starts)
    print(f"\033[{menu_start_line};1H", end='')
    print("Navegue com as setas e confirme com Enter (q para sair)".center(160))
    print(f"\033[{menu_start_line + 1};1H", end='')
    print(format_menu_line(menu_state['index']))

    while not menu_state.get('done', False):
        render_lines = []
        for y, line in enumerate(original_lines):
            new_line = []
            for c in line:
                intensity = min(0.05, 0.005 + (y / max(1, height)) * 0.02 + (step / 200) * 0.02)
                if c != ' ' and random.random() < intensity:
                    new_line.append(random.choice(list("@!:")))
                else:
                    new_line.append(c)
            render_lines.append(new_line)

        # render only title area
        print("\033[H", end='')
        
        for line in render_lines:
            colored_line = "".join(colorize_char(c) for c in line)
            # use clear-to-end to avoid remnants
            print(center_ansi(colored_line, WIDTH).ljust(WIDTH), end='\n')

        # update menu selection only when changed
        if menu_state.get('index') != last_index:
            last_index = menu_state.get('index')
            print(f"\033[{menu_start_line + 1};1H", end='')
            print(format_menu_line(last_index).ljust(WIDTH), end='')
      
        step += 1
        await asyncio.sleep(0.05)


def run_title_with_menu():
    lines, original_lines, _ = show_title()
    menu_state = {
        'index': 0,
        'done': False,
        'selection': None,
        'quit': False
    }

    input_thread = None
    try:
        import threading
        input_thread = threading.Thread(target=interact_menu, args=(menu_state,), daemon=True)
        input_thread.start()
        asyncio.run(glitch_title_with_menu(original_lines, menu_state))
    except KeyboardInterrupt:
        menu_state['done'] = True
    finally:
        if input_thread and input_thread.is_alive():
            menu_state['done'] = True
            input_thread.join(timeout=0.5)

    return menu_state.get('selection')


def introduction_main():
    pygame.mixer.init()

    hide_cursor()

    lines_to_show = [
        # "one day $$PURPLE$$you$$RESET$$ woke up",
        # "when $$PURPLE$$you$$RESET$$ looked around, nothing was the same",
        # "$$PURPLE$$you$$RESET$$ felt wrong, something was off",
        # "$$PURPLE$$You$$RESET$$ knew you were going to die."
        "^-^"
    ]

    odds = random.randint(1, 100)
    odds = 1 # force test line for now
    if odds == 1:
        lines_to_show.append(random.choice(linesEaster))

    print("\n" * 20)

    try:
        for line in lines_to_show[:-1]:
            type_line(line)
            wipe_line()

        final_line = lines_to_show[-1]
        type_line(final_line)
        final_phase(final_line)

        print("\n" * 15)

        selection = run_title_with_menu()
    finally:
        show_cursor()

    # MENU OPTIONS

    if selection is None:
        print("Menu foi cancelado. Saindo...")
    elif selection == 0: # PLAY BUTTON
        ui.draw_ui()
        
    elif selection == 1: # LOAD BUTTON
        print(color_line("$$RED$$teste$$RESET$$ de $$BLUE$$cor$$RESET$$"))

    elif selection == 2: # OPTIONS BUTTON
        print("Options selecionado")

    elif selection == 3: # EXIT BUTTON
        exit.exit_intro()


if __name__ == "__main__":
    introduction_main()
