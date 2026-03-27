import pyautogui as pg
import msvcrt
import os

index = 0
key = 0

# this code is so much cooler than i expected
def seta():
    while True:
        os.system("cls")
        # receive the info of pressed arrows on the keyboard

        if key == b'\xe0':  # Arrow keys prefix
            key = msvcrt.getch()
            if key == b'K':  # Left arrow
                index -= 1
            elif key == b'M':  # Right arrow
                index += 1
            if key == b'q':  # Quit on 'q' key
                break

        match index:
            case 0:
                opt1 = ">>"
                opt2 = "  "
                opt3 = "  "
                opt4 = "  "
            case 1:
                opt1 = "  "
                opt2 = ">>"
                opt3 = "  "
                opt4 = "  "
            case 2:
                opt1 = "  "
                opt2 = "  "
                opt3 = ">>"
                opt4 = "  "
            case 3:
                opt1 = "  "
                opt2 = "  "
                opt3 = "  "
                opt4 = ">>"
            case _:
                index = 0
                opt1 = ">>"
                opt2 = "  "
                opt3 = "  "
                opt4 = "  "

        print(f"{opt1} Start    {opt2} Load    {opt3} Options    {opt4} Exit")
        key = msvcrt.getch()
