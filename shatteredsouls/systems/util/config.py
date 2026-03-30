import os

WIDTH = 120
HEIGHT = 30

def screen_config():
    global WIDTH, HEIGHT

    os.system('cls')
    os.system(f'mode con: cols={WIDTH} lines={HEIGHT}')
