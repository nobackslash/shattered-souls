import time
import os
import random
import pygame
import asyncio
import atexit
import shutil
import re

import shatteredsouls.assets as assets
from shatteredsouls.assets.text.title import ascii_title
from shatteredsouls.systems.cutscene.style_effects import glitch_loop, center_ansi, visible_length

WIDTH = shutil.get_terminal_size().columns
HEIGHT = shutil.get_terminal_size().lines

glich_fx = "░▒▓█"
ANSI_REGEX = re.compile(r'\x1b\[[0-9;]*m')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cleanup():
    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except Exception:
        pass
    print("\033[?25h", end="")

atexit.register(cleanup)


def color_line(text):
    lower = text.lower()
    chars = list(text)
    colored = []

    i = 0
    while i < len(chars):
        if lower[i:i+3] == "you":
            for j in range(3):
                colored.append(f"\033[2;35m{chars[i+j]}\033[0m")  # dim purple
            i += 3
        elif lower[i:i+3] == "die":
            for j in range(3):
                colored.append(f"\033[31m{chars[i+j]}\033[0m")  # red
            i += 3
        else:
            colored.append(chars[i])
            i += 1

    return "".join(colored)


def type_line(text):
    current = ""
    for char in text:
        current += char
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
        print("\r" + center_ansi(f"\033[31m{glitched}\033[0m", WIDTH).ljust(WIDTH), end="", flush=True)
        time.sleep(0.1)


def final_phase(text):
    try:
        awake = pygame.mixer.Sound(assets.sfx["glitch_sfx"])
        awake.play()

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

    def base_colorize(c):
        if c == "@":
            return "\033[35m@\033[0m"
        elif c == "!":
            return "\033[2;35m!\033[0m"
        elif c == ":":
            return "\033[90m:\033[0m"
        return c

    for line in lines:
        colored = "".join(base_colorize(c) for c in line)
        print(center_ansi(colored, WIDTH))

    time.sleep(1)
    return lines, original_lines, height


def main():
    pygame.mixer.init()

    lines_to_show = [
        "one day you woke up",
        "when you looked around, nothing was the same",
        "you felt wrong, something was off",
        "You knew you were going to die."
    ]

    print("\n" * 20)

    for line in lines_to_show[:-1]:
        type_line(line)
        wipe_line()

    final_line = lines_to_show[-1]
    type_line(final_line)
    final_phase(final_line)

    print("\n" * 15)

    lines, original_lines, height = show_title()

    try:
        asyncio.run(glitch_loop(lines, height, WIDTH, original_lines))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
