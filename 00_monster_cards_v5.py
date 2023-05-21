"""Base component for the Monster Cards program

Patch notes:
v2
- Adjusted search_card() to simply return a card
v3
- When exiting REVIEW card and no changes are made, confirmation prompt removed
- Added confirmation message when saving a card
- Called welcome() in main routine
- Added confirmation prompt when exiting program
- Tried to tidy up printing a little, will work on that more later
v4
- Added choice parameter to review_card(), so that if user selects 'Edit' in
  menu, they will proceed directly to EDIT. Then, when they
  complete editing, will return to REVIEW
- Option to DELETE card from REVIEW
- Adjusted Delete Card message to make display prettier and remove the :(
v5
- Added a nybox which prioritised NO, replaced all relevant occurrences of
  ynbox with nybox
- Fixed bug: When in REVIEW of a newly created card, clicking delete would
  throw an error (simply added False to return statement)
- Added more specialised message when saving a card during REVIEW: if
  already in cat, 'changes saved,' if not yet in cat, 'saved to cat'
- Reordered functions
- Reduced code in search_card() slightly
- Replaced looping mechanics in edit_card() with a while loop, instead of
  using recursion, to reduce chance of stack overflow and increase readability

To Do:
- Bug testing
- Try printing all user actions?
- Cards in alphabetical/custom order: Printing, Choicebox

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


def nybox(msg, title):
    choice = buttonbox(msg, title, choices=["NO", "Yes"])
    return True if choice == "Yes" else False


# 01 Welcome
def welcome():
    print(f"#### WELCOME TO MONSTER CARD CATALOGUE MANAGER ####\n")
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
    print("#### ####")


# 03 Search
def find_card(name, cat=card_cat):
    """Returns the card and index that matches the name;
    thus duplicate names invalid"""
    for index, card in enumerate(cat):
        if card[0].lower() == name.lower():
            return card, index
    return None


def search_card(cat=card_cat):
    title = "Search Card"
    cards = [card[0] for card in cat]  # collect card names
    choice = choicebox("Choose a card:", title, choices=cards)

    if choice is None:
        return None

    card, _ = find_card(choice, cat)

    print(format_card(card))

    return card


# 04 Edit

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


def review_card(card, cat=card_cat, choice=None):
    title = "Review Card"
    card_temp = [card[0], card[1][:]]  # stops mutability property of lists

    while True:
        if choice is None:  # no preset action
            choice = buttonbox(format_card(card_temp), title,
                               ("Edit", "Save", "Delete", "Cancel"))

        if choice == "Edit":  # go to editing
            card_temp = edit_card(card_temp, card)

        elif choice == "Save":  # save card
            if card in cat:  # card already in catalogue:
                cat[cat.index(card)] = card_temp  # replaces card
                msgbox(f"Changes to **{card_temp[0]}** have been saved", title)
            else:
                cat.append(card_temp)  # adds card to end
                msgbox(f"**{card_temp[0]}** has been saved to the catalogue",
                       title)

            return cat

        elif choice == "Delete":
            cat, card_was_deleted = delete_card(card, cat)
            if card_was_deleted:
                return cat

        elif choice == "Cancel":  # cancel changes and exit
            if card == card_temp:  # no changes made
                confirm = True
            elif card in cat:
                confirm = nybox("Are you sure you want to cancel changes? "
                                "All changes made will be reverted", title)
            else:
                confirm = nybox("Are you sure you want to cancel? The card "
                                "has not yet been added to the catalogue, "
                                "so will be deleted", title)
            if confirm:
                return cat

        # reset loop
        choice = None


def edit_card(card, orig_card):
    title = "Edit Card"

    while True:
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
                confirm = nybox(f"Are you sure you want to cancel **"
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
        msgbox("This card does not appear in the catalogue, "
               "and so cannot be deleted", title)
        return cat, False

    confirm = nybox(format_card(card) + f"\nAre you sure you\nwant to delete\n"
                                        f"**{card[0]}**?",
                    title)
    if confirm:
        cat.remove(card)
        msgbox(f"**{card[0]}** has been deleted from the catalogue")
        return cat, True
    else:
        msgbox(f"You have just saved **{card[0]}'s** life", title)
        return cat, False


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
    avgs = get_averages(cat)

    if choice == "Names only":
        for count, card in enumerate(cat):
            print(f"{count + 1:<3}", card[0])

    elif choice == "Summary":
        print(f"   {'Average:':<15}", " ".join(f"{i:<3}" for i in avgs))
        print()
        for count, card in enumerate(cat):
            print(f"{count + 1:<3} {card[0]:<15}", " ".join(f"{i:<3}" for i in
                                                            card[1]))

    elif choice == "Full info":
        print(format_card(["AVERAGES", avgs], "--"))
        for count, card in enumerate(cat):
            print(format_card(card, count=count + 1))


# 00 Main Menu
def main(cat=card_cat):
    title = "Monster Card Catalogue Manager"
    choice = buttonbox("What next?", title,
                       choices=["Create card", "Edit card", "Delete card",
                                "Search card", "Output catalogue", "Exit"])
    if choice == "Exit":
        confirm = nybox("Are you sure you want to exit the program?", title)
        if confirm:
            msgbox("Your catalogue has been stored in the variable 'card_cat'",
                   "Exit")
            return cat

    elif choice == "Create card":
        cat = create_card(cat)

    elif choice == "Edit card":
        card = search_card(cat)
        cat = review_card(card, cat, "Edit")

    elif choice == "Delete card":
        card = search_card(cat)
        cat, _ = delete_card(card, cat)

    elif choice == "Search card":
        card = search_card(cat)
        cat = review_card(card, cat)

    elif choice == "Output catalogue":
        output_cards(cat)

    return main(cat)


# Main routine
welcome()
card_cat = main(card_cat)
