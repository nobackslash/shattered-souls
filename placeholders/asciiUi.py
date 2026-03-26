import os
"""This file contains the ASCII UI elements for the game, such as borders, dividers, and other decorative elements."""
"""
╚ ╔ ╩ ╦ ╠ ═ ╬ ╣ ║ ╗ ╝
"""

def draw_ui(location: str, player_name: str = "Carambalamba"):
    name_level = f"{player_name.capitalize()}, Level - 0".center(120)
    print(f"""
╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
{location.upper().center(120)}
{name_level}
╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣




















╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
          


╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""")
    
if __name__ == "__main__":
    os.system("cls")
    draw_ui("Yharnam Central Street")