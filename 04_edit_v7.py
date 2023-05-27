"""Component 04: Edit cards

Restarted the code, based off two functions: review and edit.
Although functionality is not fully implemented, the basics of Edit, Save, 
and Cancel in review_card() work, and the returned card_cat is correct.

The .copy() method I used in review_card() to make a copy of the list does
not work, because it creates a shallow copy. This means that the outer list,
i.e. [Name, Traits] is a copy, but traits = [0, 0, 0, 0,] is a reference.
Instead, used: card_temp = [card[0], card[1][:]]

I have corrected the code for setting attributes in edit_card() and added a
confirmation prompt when cancelling.

Renamed TITLE to title to meet PEP8 requirements.

Fixed bug where canceling during rename would set name to None

Removed redundant find_card() function, and fixed the one use-case

Fixed bug where you couldn't rename the card to its original name, because
it showed the error "card already in catalogue" with a patchwork fix

Added capitalisation to renaming card
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


def get_new_name(msg, title, orig_card, cat=card_cat):
    """Returns a str; the new name"""
    cards = [card[0] for card in cat]  # collect card names

    new_name = enterbox(msg, title)

    if not new_name:
        return None
    new_name = new_name.capitalize()

    if new_name not in cards or new_name == orig_card[0]:
        return new_name
    else:
        msgbox(f"There is already a monster named *{new_name}* in the "
               f"catalogue. Please choose another name.", "Edit Card")
        return get_new_name(msg, title, orig_card, cat)


def set_new_trait(msg, title, current_value=None):
    """Returns an int; the new trait value"""
    new_value = integerbox(msg + f"\n\nMust be an integer between {MIN_TRAIT} "
                                 f"and {MAX_TRAIT}",
                           title, upperbound=MAX_TRAIT, lowerbound=MIN_TRAIT)
    if new_value is None and current_value is not None:
        return current_value

    return new_value


def format_card(card):
    """Returns card details as a str"""
    msg = f"**{card[0]}**\n"
    for index, trait in enumerate(card[1]):
        msg += f" {TK[index]}: {trait}\n"
    return msg


def review_card(card, cat=card_cat):
    title = "Review Card"
    card_temp = [card[0], card[1][:]]  # stops mutability property of lists

    while True:

        choice = buttonbox(format_card(card_temp), title,
                           ("Edit", "Save", "Cancel"))

        if choice == "Edit":  # go to editing
            card_temp = edit_card(card_temp, card)

        elif choice == "Save":  # save card
            if card in cat:  # card already in catalogue:
                cat[cat.index(card)] = card_temp  # replaces card
            else:
                cat.append(card_temp)  # adds card to end
            return cat

        elif choice == "Cancel":  # cancel changes and exit
            if card in cat:
                confirm = ynbox("Are you sure you want to cancel changes? "
                                "All changes made will be reverted", title)
            else:
                confirm = ynbox("Are you sure you want to cancel? The card "
                                "has not yet been added to the catalogue, "
                                "so will be deleted", title)
            if confirm:
                return cat
            # else restart loop


def edit_card(card, orig_card):
    title = "Edit Card"
    choice = buttonbox(format_card(card), title,
                       choices=("Rename", *TK, "Done"))

    if choice == "Rename":  # edit name
        new_name = get_new_name(f"Rename {card[0]}", title, orig_card)
        if new_name:
            card[0] = new_name

        return edit_card(card, orig_card)

    elif choice == "Done":  # return card
        return card

    else:  # edit trait

        msg = f"**{card[0]}'s** {choice}: {card[1][TK.index(choice)]}\n\n" \
              f"Set a new value"

        card[1][TK.index(choice)] = set_new_trait(msg, title, card[1][
            TK.index(choice)])

        return edit_card(card, orig_card)


# ["Newcard", [2, 2, 2, 2]]
# card_cat[0]
card_cat = review_card(card_cat[0], card_cat)
print(card_cat)
