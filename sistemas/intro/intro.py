# import util
import time
import os
import random
from turtle import clear
import pygame
# from util.config import WIDTH, HEIGHT
from asciiTitle import tituloLargo

WIDTH = 120
HEIGHT = 30

text1 = "one day you woke up"
text2 = "when you looked around, nothing was the same"
text3 = "you felt wrong, something was off"
text4 = "you knew you were going to die."
glich_fx = "░▒▓█"

# text1 = "debug1"
# text2 = "debug2"
# text3 = "debug3"
# text4 = "debug4"

def show_title():
    pygame.mixer.music.load("moonlight reversed.mp3")
    pygame.mixer.music.play()

    original_lines = [list(line) for line in tituloLargo.split("\n")]
    lines = [row.copy() for row in original_lines]
    height = len(lines)

    for line in lines:
        print("".join(line).center(WIDTH))

    time.sleep(1)

    return lines, original_lines, height


def print_title_cutscene(text: str, final = False):
    global WIDTH, HEIGHT

    os.system("cls")
    print("\n" * 13)
    index = 1
    text_string = ""

    for i in text:
        index += 1
        text_string += i

        if final == False:
            print(text_string.center(WIDTH), end="\r")
            time.sleep(0.09)
        else:
            print(f"\033[31m{text_string}\033[0m".center(WIDTH), end="\r")
            time.sleep(0.09)
        

    if final == False:
        time.sleep(1)
    else:       
        time.sleep(3)

    if final == True:
        for i in range(10):
            intensity = (i + 1) / 10
            glitched = glitch_effect(text_string, intensity=intensity)
            visible_chars = int(len(text_string) * (1 - intensity))
            glitched = glitched[:visible_chars]
            print(f"\033[31m{glitched}\033[0m".center(WIDTH), end="\r")
            time.sleep(0.2)
        play_awake_cut()

def glitch_effect(text: str, intensity: float = 0.1) -> str:
    global glich_fx

    glitched_text = ""
    for char in text:
        if random.random() < intensity: # chance of glitching each character
            glitched_text += random.choice(glich_fx)
        else:
            glitched_text += char

    return glitched_text

def play_awake_cut():
    awake = pygame.mixer.Sound("awake.mp3")
    awake.play()

    clear()
    time.sleep(awake.get_length())
    clear()


def full_title_animation():
    

    print_title_cutscene(text1)
    time.sleep(1)
    print_title_cutscene(text2)
    time.sleep(1)
    print_title_cutscene(text3)
    time.sleep(1)
    print_title_cutscene(text4, final=True)
    time.sleep(2)

    lines, original_lines, height = show_title()

if __name__ == "__main__": # Debug only
    pygame.mixer.init()
    awake = pygame.mixer.Sound("awake.mp3")
    awake.play()
    
    full_title_animation()
    time.sleep(5)