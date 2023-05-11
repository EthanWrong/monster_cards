"""Component 06: Delete Cards

Code that allows the user to delete a card from the catalogue

Updated text printing
"""

from easygui import *

TK = ["Strength", "Speed", "Stealth", "Cunning"]  # Trait Key

MAX_TRAIT, MIN_TRAIT = 25, 1  # maximum and minimum values for traits

card_cat = [  # card catalogue
    ["Stoneling", [7, 1, 25, 15]],
    ["Vexscream", [1, 6, 21, 19]],
    ["Dawnmirage", [5, 15, 18, 22]],
    ["Blazegolem", [15, 20, 23, 6]],
    ["Websnake", [7, 15, 10, 5]],
    ["Moldvine", [21, 18, 14, 5]],
    ["Vortexwing", [19, 13, 19, 2]],
    ["Rotthing", [16, 7, 4, 12]],
    ["Froststep", [14, 14, 17, 4]],
    ["Wispghoul", [17, 19, 3, 2]],
]


def format_card(card):
    """Returns card details as a str"""
    msg = f"**{card[0]}**\n"
    for index, trait in enumerate(card[1]):
        msg += f" {TK[index]}: {trait}\n"
    return msg


def delete_card(card, cat=card_cat):
    title = "Delete Card"
    confirm = ynbox(format_card(card)+f"\nAre you sure you want to delete "
                                      f"**{card[0]}**?\n\nThey will be very "
                                      f"sad :(",
                    title)
    if confirm:
        cat.remove(card)
        return cat
    else:
        msgbox(f"You have just saved **{card[0]}'s** life", title)
        return cat


delete_card(card_cat[0], card_cat)
print(card_cat)
