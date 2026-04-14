def color_line(text: str):
    color_keys = {
        "$$PURPLE$$": "purple",
        "$$RED$$": "red",
        "$$GREEN$$": "green",
        "$$BLUE$$": "blue",
        "$$YELLOW$$": "yellow",
        "$$WHITE$$": "white",
        "$$BLACK$$": "black",
        "$$RESET$$": "reset"
    }

    color_codes = {
        "red": "\033[31m",
        "purple": "\033[35m",
        "dim_purple": "\033[2;35m",
        "green": "\033[32m",
        "blue": "\033[34m",
        "yellow": "\033[33m",
        "white": "\033[37m",
        "black": "\033[30m",
        "reset": "\033[0m"
    }

    # THE CODE BELOW IS JUST FOR STORING, WE'LL USE THE SYSTEM ABOVE

    for key, color in color_keys.items():
        text = text.replace(key, color_codes[color])

    

    return text

    try:
        for key in colorArg:
            if key in colorArg:
                colorArg[key] = color_codes[colorArg[key]]
            else:
                raise ValueError(f"Color argument for '{key}' is missing.")
    except KeyError as e:
        raise KeyError(f"Invalid color name: {e.args[0]}. Valid options are: {', '.join(color_codes.keys())}")

    lower = text.lower()
    chars = list(text)
    colored = []

    i = 0

    while i < len(chars):
        if any(lower[i:i+len(word)] == word for word in colorArg):
            matched_word = next(word for word in colorArg if lower[i:i+len(word)] == word)
            color_code = colorArg[matched_word]
            for j in range(len(matched_word)):
                colored.append(f"{color_code}{chars[i+j]}{color_codes['reset']}")  # apply specified color
            i += len(matched_word)
        else:
            colored.append(chars[i])
            i += 1
    return "".join(colored)

text = color_line("$$PURPLE$$This is a test line with colored$$RESET$$ words.$$GREEN$$ Enjoy!$$RESET$$")
print(text)