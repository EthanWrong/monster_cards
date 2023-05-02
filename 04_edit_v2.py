"""Component 04: Edit cards

Created basic editing functionality; a card is passed into edit_card() which
 handles editing until 'Done' is clicked

Updated the TK and made code slightly more efficient"""

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
    new_value = integerbox(msg+f"\n\nMust be an integer between {MIN_TRAIT} "
                               f"and {MAX_TRAIT}",
                           title, upperbound=MAX_TRAIT, lowerbound=MIN_TRAIT)
    if new_value is None and current_value is not None:
        return current_value

    return new_value


def edit_card(card, cat=card_cat):
    traits = ["Rename", *TK, "Done"]  # creates buttons

    # Display details as str
    msg = f"**{card[0]}**\n"
    for index, trait in enumerate(card[1]):
        msg += f" {TK[index]}: {trait}\n"

    choice = buttonbox(msg, "Edit Card", choices=traits)

    if choice == "Rename":
        card[0] = get_new_name(f"Rename {card[0]}", "Edit Card", cat)
        print(card)
        return edit_card(card)
    elif choice == "Done":
        return card
    else:
        # set new value for selected trait

        msg = f"**{card[0]}'s** {choice}: {card[1][TK.index(choice)]}\n\n" \
              f"Set a new value"
        card[1][TK.index(choice)] = set_new_trait(msg, "Edit Card", card[1][
            TK.index(choice)])
        print(card)
        return edit_card(card)


my_card = edit_card(card_cat[0])
print("my card", my_card)
