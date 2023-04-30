"""Component 03: Search for cards within a catalogue.

Trial 1: Buttons"""

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

    ["Websdnake", [7, 15, 10, 5]],
    ["Moldveine", [21, 18, 14, 5]],
    ["Vortexfwing", [19, 13, 19, 2]],
    ["Rotthingg", [16, 7, 4, 12]],
    ["Froststehp", [14, 14, 17, 4]],
    ["Viexscream", [1, 6, 21, 19]],
    ["Dajwnmirage", [5, 15, 18, 22]],
    ["Blakzegolem", [15, 20, 23, 6]],
    ["Webslnake", [7, 15, 10, 5]],
    ["Moldvmine", [21, 18, 14, 5]],
    ["Vortexnwing", [19, 13, 19, 2]],
    ["Rotthinog", [16, 7, 4, 12]],
    ["Froststepp", [14, 14, 17, 4]],
    ["Vexscreamq", [1, 6, 21, 19]],
    ["Drawnmirage", [5, 15, 18, 22]],
    ["Blsazegolem", [15, 20, 23, 6]],
    ["Webtsnake", [7, 15, 10, 5]],
    ["Molduvine", [21, 18, 14, 5]],
    ["Vortevxwing", [19, 13, 19, 2]],
    ["Rotthiwng", [16, 7, 4, 12]],
    ["Froststxep", [14, 14, 17, 4]],
]


def search_card(cat=card_cat):
    cards = []
    for card in cat:
        cards.append(card[0])
    buttonbox("Choose a card:", choices=cards)


search_card()
