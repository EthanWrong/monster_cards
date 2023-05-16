"""Component 01: Welcome + Instructions"""

from easygui import *

TK = ["Strength", "Speed", "Stealth", "Cunning"]  # Trait Key

MAX_TRAIT, MIN_TRAIT = 25, 1  # maximum and minimum values for traits

def welcome():
    print("#### WELCOME TO MONSTER CARD CATALOGUE MANAGER ####")
    print()
    msg = f"Welcome to the wonderful world of MONSTER CARDS!\n\nWould you " \
          f"like to see the instructions?"
    choice = ynbox(msg, "Welcome")
    if choice:
        instructions()


def instructions():
    messages = [
        f"This program allows you to store and manage monster cards in the "
        f"catalogue.\n\nYou may EDIT or DELETE cards, and can OUTPUT the "
        f"full menu to the Python Console.",
        f"Cards are attached to a name, and then have {len(TK)} traits.\n\n"
        f"The traits each card can have are {', '.join(TK)}.\n\n"
        f"The traits have an integer value between {MIN_TRAIT} and "
        f"{MAX_TRAIT}",
        f"That's it, really!"
    ]

    print("#### INSTRUCTIONS ####")
    for i in messages:
        print(i, "\n")
        msgbox(i, "Instructions")


welcome()
