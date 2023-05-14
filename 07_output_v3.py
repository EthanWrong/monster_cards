"""Component 07: Output cards

Prints all cards to catalogue, giving option for user to print:
 Just names:
 Stoneling

 or Summary:
 Stoneling 7 1 25 15

 or Full info:
 **Stoneling**
 Strength: 7
 Speed: 1
 Stealth: 25
 Cunning: 15


Added summary option
Added average stats
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


def format_card(card, d="**"):
    """Returns card details as a str"""
    msg = f"{d}{card[0]}{d}\n"
    for index, trait in enumerate(card[1]):
        msg += f" {TK[index]}: {trait}\n"
    return msg


def get_averages(cat):
    averages = []
    for trait in TK:
        total = 0
        for card in cat:
            total += card[1][TK.index(trait)]
        averages.append(round(total/len(cat)))

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
        for card in cat:
            print(card[0])

    elif choice == "Summary":
        avgs = get_averages(cat)
        print(f"{'Average:':<15}", " ".join(f"{i:<3}" for i in avgs))
        print()
        for card in cat:
            print(f"{card[0]:<15}", " ".join(f"{i:<3}" for i in card[1]))

    elif choice == "Full info":
        print(format_card(["AVERAGES", get_averages(cat)], "--"))
        for card in cat:
            print(format_card(card))


output_cards(card_cat)
