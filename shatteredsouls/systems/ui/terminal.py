import os
try:
    import ctypes
except Exception:
    ctypes = None

# Criado pelo chatgpt para esconder e aparecer o cursor do terminal, para tirar aquele bloco branco feio na tela.
def hide_cursor():
    """Hide the terminal cursor cross-platform.

    On Windows this uses the Console API via ctypes; on other platforms
    it emits the ANSI hide-cursor sequence.
    """
    try:
        if os.name == 'nt' and ctypes:
            h = ctypes.windll.kernel32.GetStdHandle(-11)
            class CONSOLE_CURSOR_INFO(ctypes.Structure):
                _fields_ = [('dwSize', ctypes.c_uint), ('bVisible', ctypes.c_bool)]
            ci = CONSOLE_CURSOR_INFO()
            if ctypes.windll.kernel32.GetConsoleCursorInfo(h, ctypes.byref(ci)):
                ci.bVisible = False
                ctypes.windll.kernel32.SetConsoleCursorInfo(h, ctypes.byref(ci))
        else:
            print('\033[?25l', end='', flush=True)
    except Exception:
        # best-effort; don't raise from UI helper
        pass


def show_cursor():
    """Show the terminal cursor (inverse of hide_cursor)."""
    try:
        if os.name == 'nt' and ctypes:
            h = ctypes.windll.kernel32.GetStdHandle(-11)
            class CONSOLE_CURSOR_INFO(ctypes.Structure):
                _fields_ = [('dwSize', ctypes.c_uint), ('bVisible', ctypes.c_bool)]
            ci = CONSOLE_CURSOR_INFO()
            if ctypes.windll.kernel32.GetConsoleCursorInfo(h, ctypes.byref(ci)):
                ci.bVisible = True
                ctypes.windll.kernel32.SetConsoleCursorInfo(h, ctypes.byref(ci))
        else:
            print('\033[?25h', end='', flush=True)
    except Exception:
        pass


__all__ = ["hide_cursor", "show_cursor"]
