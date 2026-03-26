import random
import asyncio
import re

glitch_chars = list("@!:")

ANSI_REGEX = re.compile(r'\x1b\[[0-9;]*m')


def visible_length(text):
    return len(ANSI_REGEX.sub('', text))


def center_ansi(text, width):
    real_len = visible_length(text)
    padding = max(0, (width - real_len) // 2)
    return " " * padding + text


# -------- Colorização dos caracteres --------

def colorize_char(c):
    if c == "@":
        return "\033[35m@\033[0m"     # Roxo
    elif c == "!":
        return "\033[2;35m!\033[0m"   # Roxo
    elif c == ":":
        return "\033[90m:\033[0m"     # Cinza
    return c


# -------- Loop principal --------

async def glitch_loop(lines, height, width, original_lines):
    step = 0

    while True:
        render_lines = []

        for y, line in enumerate(original_lines):
            new_line = []

            for x, char in enumerate(line):
                intensity = min(
                    0.05,
                    0.005 + (y / height) * 0.02 + (step / 200) * 0.02
                )

                if char != " " and random.random() < intensity:
                    new_line.append(random.choice(glitch_chars))
                else:
                    new_line.append(char)

            render_lines.append(new_line)

        print("\033[H", end='')

        colored_lines = []
        for line in render_lines:
            colored_line = "".join(colorize_char(c) for c in line)
            colored_lines.append(center_ansi(colored_line, width))

        print("\n" * 15)
        print("\n".join(colored_lines))

        step += 1
        await asyncio.sleep(0.05)