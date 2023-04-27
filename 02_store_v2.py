"""Component 02: Store cards in catalogue.
NOTES: No duplicate names within catalogue.

Some helpful functions added for easier data management.

Because this assessment only requires manipulation of one variable,
'card_cat', I have coded it in at the start and have made functions default
to using card_cat as the catalogue to search in. To use another catalogue,
simply name that catalogue in the parameters.
THIS MEANS card_cat MUST BE DECLARED BEFORE FUNCTIONS"""


TK = {"Strength": 0, "Speed": 1, "Stealth": 2, "Cunning": 3}  # Trait Key

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
    ["Wispghoul", [17, 19, 3, 2]]
]


def find_card(name, cat=card_cat):
    """Returns the card and index that matches the name;
    thus duplicate names invalid"""
    for index, card in enumerate(cat):
        if card[0].lower() == name.lower():
            return card, index
    return None


def find_trait(trait, card):
    return card[1][TK[trait]]  # 1 is the index for the traits list


my_card, my_card_index = find_card("Rotthing")
my_trait = find_trait("Stealth", my_card)

print("my_card:", my_card)
print("my_card_index:", my_card_index)
print("my_trait:", my_trait)
