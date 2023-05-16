"""Base component for the Monster Cards program
Copied code from:
01_welcome_v1
02_store_v2
03_store_v3
04_edit_v7
05_create_v2
06_delete_v3
07_output_v4

Used the latest versions of the following functions:
format_card() from 07v4
edit_card() from 05v2
review_card() from 05_v2
get_new_name() from 05v2
set_new_trait() from 05v2
find_card() from 03v3

TK, MAX_TRAIT, MIN_TRAIT, card_cat are all copied from 04v7

Simply copied/pasted these components together, no functionality or main
routine yet.
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


def format_card(card, d="**", count=None):
    """Returns card details as a str"""
    msg = f"{count:<3}{d}{card[0]}{d}\n" if count else f"{d}{card[0]}{d}\n"
    for index, trait in enumerate(card[1]):
        msg += f"   {TK[index]}: {trait}\n" if count else f" {TK[index]}:" \
                                                          f" {trait}\n"
    return msg


def get_new_name(msg, title, orig_card=None, cat=card_cat):
    """Returns a str; the new name"""
    cards = [card[0] for card in cat]  # collect card names

    new_name = enterbox(msg, title)

    if not new_name:
        return None
    new_name = new_name.capitalize()

    if new_name not in cards or orig_card and new_name == orig_card[0]:
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


def find_card(name, cat=card_cat):
    """From 02_store_v2.py"""
    """Returns the card and index that matches the name;
    thus duplicate names invalid"""
    for index, card in enumerate(cat):
        if card[0].lower() == name.lower():
            return card, index
    return None


# 01 Welcome
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


# 03 Search
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


# 04 Edit
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


# 05 Create
def create_card(cat=card_cat):
    title = "Create Card"
    name = get_new_name("Enter a name for your new monster card",
                        title)
    if name is None:
        msgbox("You have exited the Create Card process", title)
        return cat

    traits = []
    for trait in TK:
        while True:
            msg = f"Set **{name}'s** {trait} trait"
            new_trait = set_new_trait(msg, title)
            if new_trait is None:
                confirm = ynbox(f"Are you sure you want to cancel **"
                                f"{name}'s** creation?", title)
                if confirm:
                    return cat
            else:
                traits.append(new_trait)
                break

    return review_card([name, traits], cat)


# 06 Delete
def delete_card(card, cat=card_cat):
    title = "Delete Card"
    if card not in cat:
        msgbox("Imposter! This card does not appear in the catalogue, "
               "and so cannot be deleted", title)
        return cat

    confirm = ynbox(format_card(card) + f"\nAre you sure you want to delete "
                                        f"**{card[0]}**?\n\nThey will be very "
                                        f"sad :(",
                    title)
    if confirm:
        cat.remove(card)
        return cat
    else:
        msgbox(f"You have just saved **{card[0]}'s** life", title)
        return cat


# 07 Output
def get_averages(cat):
    averages = []
    for trait in TK:
        total = 0
        for card in cat:
            total += card[1][TK.index(trait)]
        averages.append(round(total / len(cat)))

    return averages


def output_cards(cat=card_cat):
    title = "Output Cards"
    choice = buttonbox("What would you like to print?", title,
                       choices=["Names only", "Summary", "Full info",
                                "Cancel"])
    if choice == "Cancel":
        return
    print("#### MONSTER CARD CATALOGUE ####")
    print(f" Total cards: {len(cat)}\n")

    if choice == "Names only":
        for count, card in enumerate(cat):
            print(f"{count + 1:<3}", card[0])

    elif choice == "Summary":
        avgs = get_averages(cat)
        print(f"   {'Average:':<15}", " ".join(f"{i:<3}" for i in avgs))
        print()
        for count, card in enumerate(cat):
            print(f"{count + 1:<3} {card[0]:<15}", " ".join(f"{i:<3}" for i in
                                                            card[1]))

    elif choice == "Full info":
        print(format_card(["AVERAGES", get_averages(cat)], "--"))
        for count, card in enumerate(cat):
            print(format_card(card, count=count + 1))
