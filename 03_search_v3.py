"""Component 03: Search for cards within a catalogue.

Using a choicebox.
User selects a card, and it returns that card plus an action. If cancel is
clicked, returns the action 'back'.
These returned actions will be used in the final assembled outcome.

Updated the TK
Updated the TK again"""

from easygui import *

TK = ["Strength", "Speed", "Stealth", "Cunning"]  # Trait Key

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

    # ["Vaexscream", [1, 6, 21, 19]],
    # ["Dabwnmirage", [5, 15, 18, 22]],
    # ["Blaczegolem", [15, 20, 23, 6]],
    # ["Websdnake", [7, 15, 10, 5]],
    # ["Moldveine", [21, 18, 14, 5]],
    # ["Vortexfwing", [19, 13, 19, 2]],
    # ["Rotthingg", [16, 7, 4, 12]],
    # ["Froststehp", [14, 14, 17, 4]],
    # ["Viexscream", [1, 6, 21, 19]],
    # ["Dajwnmirage", [5, 15, 18, 22]],
    # ["Blakzegolem", [15, 20, 23, 6]],
    # ["Webslnake", [7, 15, 10, 5]],
    # ["Moldvmine", [21, 18, 14, 5]],
    # ["Vortexnwing", [19, 13, 19, 2]],
    # ["Rotthinog", [16, 7, 4, 12]],
    # ["Froststepp", [14, 14, 17, 4]],
    # ["Vexscreamq", [1, 6, 21, 19]],
    # ["Drawnmirage", [5, 15, 18, 22]],
    # ["Blsazegolem", [15, 20, 23, 6]],
    # ["Webtsnake", [7, 15, 10, 5]],
    # ["Molduvine", [21, 18, 14, 5]],
    # ["Vortevxwing", [19, 13, 19, 2]],
    # ["Rotthiwng", [16, 7, 4, 12]],
    # ["Froststxep", [14, 14, 17, 4]]
]


def find_card(name, cat=card_cat):
    """From 02_store_v2.py"""
    """Returns the card and index that matches the name;
    thus duplicate names invalid"""
    for index, card in enumerate(cat):
        if card[0].lower() == name.lower():
            return card, index
    return None


def search_card(action, cat=card_cat):
    # collect card names
    cards = []
    for card in cat:
        cards.append(card[0])

    choice = choicebox("Choose a card:", choices=cards)

    if choice is None:
        return "back"  # go back a dialogue

    card, _ = find_card(choice, cat)

    # print card
    print(card[0])
    for index, trait in enumerate(card[1]):
        print(TK[index], trait)

    return card, action  # in final program, will return a function e.g.
    # edit_card()


print("returned value:", search_card("edit"))
