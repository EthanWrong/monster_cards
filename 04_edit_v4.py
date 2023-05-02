"""Component 04: Edit cards

Restarted the code, based off two functions: review and edit.
Although functionality is not fully implemented, the basics of Edit, Save, 
and Cancel in review_card() work, and the returned card_cat is correct."""

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


def find_card(name, cat=card_cat):
    """From 02_store_v2.py"""
    """Returns the card and index that matches the name;
    thus duplicate names invalid"""
    for index, card in enumerate(cat):
        if card[0].lower() == name.lower():
            return card, index
    return None


def get_new_name(msg, title, cat):
    # collect card names
    cards = []
    for card in cat:
        cards.append(card[0])

    new_name = enterbox(msg, title)
    if new_name not in cards:
        return new_name
    else:
        msgbox(f"There is already a monster named *{new_name}* in the "
               f"catalogue. Please choose another name.", "Edit Card")
        return get_new_name(msg, title, cat)


def set_new_trait(msg, title, current_value=None):
    print(52, card_cat)
    new_value = integerbox(msg + f"\n\nMust be an integer between {MIN_TRAIT} "
                                 f"and {MAX_TRAIT}",
                           title, upperbound=MAX_TRAIT, lowerbound=MIN_TRAIT)
    if new_value is None and current_value is not None:
        return current_value

    print(59, card_cat)
    return new_value


def format_card(card):
    """Returns card details as a str"""
    msg = f"**{card[0]}**\n"
    for index, trait in enumerate(card[1]):
        msg += f" {TK[index]}: {trait}\n"
    return msg


def review_card(card, cat=card_cat):
    card_temp = card.copy()  # stops mutability property of lists affecting

    while True:

        choice = buttonbox(format_card(card_temp), "Review Card",
                           ("Edit", "Save", "Cancel"))

        if choice == "Edit":
            # go to editing
            card_temp = edit_card(card_temp)
            print(card_temp)

        elif choice == "Save":  # save card
            if card in cat:  # card already in catalogue:
                cat[find_card(card[0])[1]] = card_temp  # replaces card
            else:
                cat.append(card_temp)  # adds card to end
            return cat

        elif choice == "Cancel":  # cancel changes and exit
            return cat


def edit_card(card, cat=card_cat):
    choice = buttonbox(format_card(card), "Edit Card",
                       choices=("Rename", *TK, "Done"))

    """
    if choice == "Rename":
        # allow user to rename

    elif choice == "Done":
        # return card

    else:
        #allow user to edit trait
    
    """
    return ["xxx", [1, 1, 1, 1]]


card_cat = review_card(["yyy", [2, 2, 2, 2]], card_cat)
print(card_cat)
