"""Component 03: Search for cards within a catalogue.

Trial 3: Enterbox"""

from easygui import *

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


def search_card(cat=card_cat):
    cards = []
    for card in cat:
        cards.append(card[0])

    while True:
        user = enterbox("Enter name of monster:")
        for card in cards:
            if card.lower() == user.lower():
                msgbox(f"found, {card}")
                return
        msgbox("card not found")


search_card()
