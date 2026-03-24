import random
import time
import sys

from asciiTitulo import tituloLargo
import armas

title = titulo
symbols = "!:;@"

DARK_RED    = "\033[31m"
PURPLE      = "\033[35m"   # ← changed
COLOR       = PURPLE
RESET       = COLOR

lines = title.split("\n")
num_lines = len(lines)

def glitch_frame(lines, intensity=0.3):
    glitched = []
    for line in lines:
        new_line = ""
        for c in line:
            if random.random() < intensity and c != " ":
                new_line += random.choice(symbols)
            else:
                new_line += c
        glitched.append(new_line)
    return "\n".join(glitched)

i = 0
while True:
    frame = glitch_frame(lines, 0.35 if i % 5 else 0.7)

    # Move cursor up to overwrite previous frame
    if i != 0:
        sys.stdout.write(f"\033[{num_lines}F")

    i += 1
    sys.stdout.write(COLOR + frame + RESET + "\n")
    sys.stdout.flush()
    time.sleep(0.15)

# # Final clean reveal
# sys.stdout.write(f"\033[{num_lines}F")
# sys.stdout.write(COLOR + title + RESET + "\n")
