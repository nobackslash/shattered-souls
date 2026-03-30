import pyautogui as pg
import msvcrt
import os
import time

runFlag = True
key = None
arrowFlag = False
index = 0
PURPLE = "\033[35m"
RESET = "\033[0m"

def Start():
    print("HELLO WORLD :)))))")
def Load():
    pass
def Options():
    pass
def Exit():
    global runFlag
    runFlag = False
    os.system("cls")
    print("GOODBYE A")

options = [Start, Load, Options, Exit]


def menu():
    string = ""
    global key, arrowFlag, index
    change = True  
    while runFlag:
        if change:
            change = False
            os.system("cls")

        string = ""

        if key == b'\xe0' or arrowFlag == True:  # Arrow keys prefix
            arrowFlag = True
            if key == b'K':  # Left arrow
                arrowFlag = False
                if index < 1:
                    index = 4
                index -= 1
                change = True
            elif key == b'M':  # Right arrow
                arrowFlag = False
                if index > 2:
                    index = -1
                index += 1    
                change = True



        for i in options:
            if options.index(i) == index:
                # print("PURPLE")
                optionString = f"{PURPLE}{i.__name__}{RESET} "
                string += optionString 
                continue
            optionString = f"{i.__name__} "
            string += optionString


            
            # print(options.index(i))

        print(string + " " + str(index), end="\r")
        if key == b'\r':
            options[index]()
            
        key = msvcrt.getch()



menu()
# import pyautogui as pg
# import msvcrt
# import os
# import time

# index = 0
# key = None
# selected_option = None
# # this code is so much cooler than i expected
# def check_selection_if_true():
#     global selected_option
#     match selected_option:
#         case 0:
#             print("Starting the game...")
#             # Add your game starting code here
#         case 1:
#             print("Loading the game...")
#             # Add your game loading code here
#         case 2:
#             print("Opening options...")
#             # Add your options code here
#         case 3:
#             print("Exiting the game...")
#             return True
#     return False

# def seta():
#     global key, index, selected_option
#     while True:
#         os.system("cls")
#         # receive the info of pressed arrows on the keyboard

#         if key == b'\xe0':  # Arrow keys prefix
#             key = msvcrt.getch()  # Get the actual arrow key code
#             if key == b'K':  # Left arrow
#                 index -= 1
#             elif key == b'M':  # Right arrow
#                 index += 1
#             elif key == b'q':  # Quit on 'q' key
#                 break
        
#         if key == b'\r':  # Enter key
#             print(f"You selected option {index + 1}")
#             time.sleep(3)
#             selected_option = index
#             break

#         selected = check_selection_if_true()
#         if selected:
#             break
        
#         match index:
#             case 0:
#                 opt1 = "\033[95mStart\033[0m"
#                 opt2 = "Load"
#                 opt3 = "Options"
#                 opt4 = "Exit"
#             case 1:
#                 opt1 = "Start"
#                 opt2 = "\033[95mLoad\033[0m"
#                 opt3 = "Options"
#                 opt4 = "Exit"
#             case 2:
#                 opt1 = "Start"
#                 opt2 = "Load"
#                 opt3 = "\033[95mOptions\033[0m"
#                 opt4 = "Exit"
#             case 3:
#                 opt1 = "Start"
#                 opt2 = "Load"
#                 opt3 = "Options"
#                 opt4 = "\033[95mExit\033[0m"
#             case _ if index > 3:
#                 index = 0
#                 opt1 = "\033[95mStart\033[0m"
#                 opt2 = "Load"
#                 opt3 = "Options"
#                 opt4 = "Exit"

#             case _ if index < 0:
#                 index = 3
#                 opt1 = "Start"
#                 opt2 = "Load"
#                 opt3 = "Options"
#                 opt4 = "\033[95mExit\033[0m"

#         print(f"{opt1} {opt2} {opt3} {opt4}".center(160))
#         key = msvcrt.getch()

# seta()