import os
import time
import ctypes

while True:
    os.system("cls")
    size = os.get_terminal_size()
    print(f"Width: {size.columns}, Height: {size.lines}\n" + "=" * size.columns, end="\r")
    time.sleep(1)



